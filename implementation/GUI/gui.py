from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.GUI.MplCanvas import MplCanvas
from implementation.GUI.scene import Scene
from implementation.GUI.w_main_window import Ui_w_MainWindow
from implementation.backend import Backend

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MplCanvas(FigureCanvas):
    def __init__(self, figure):
        super().__init__(figure)


class GUI(qtw.QWidget, Ui_w_MainWindow):
    def __init__(self, backend: Backend):

        # startup
        super().__init__()
        self.setupUi(self)

        # backend and state
        self.backend = backend
        self.reference_points = []
        self.image_path = None
        self.generated_charts = {}

        # self.rotation = 0  # indicates graphicsview rotation in degrees; it's needed for placeholder points

        # things in the graphics area
        self.image = None  # qtg.QPixmap

        # VALIDATING INPUT
        int_validator = qtg.QIntValidator()
        double_validator = qtg.QDoubleValidator()
        self.le_referenceMM.setValidator(int_validator)
        self.le_LeftEyeMM.setValidator(double_validator)
        self.le_RightEyeMM.setValidator(double_validator)
        self.le_UpperLipMM.setValidator(double_validator)

        self.le_LeftEyeMMChart.setValidator(double_validator)
        self.le_RightEyeMMChart.setValidator(double_validator)
        self.le_UpperLipMMChart.setValidator(double_validator)

        self.diagram = None  # MLP growth chart

        # Photo Scene Creation
        self.photoScene = Scene()
        self.photoGraphicsView.setScene(self.photoScene)
        # making sure that the scene is always in the center of photoGraphicsView
        self.photoGraphicsView.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.photoGraphicsView.setResizeAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.photoGraphicsView.setTransformationAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)

        # # Diagram Scene Creation
        # self.chartScene = qtw.QGraphicsScene()
        # self.chartGraphicsView.setScene(self.chartScene)
        # # making sure that the scene is always in the center of photoGraphicsView
        # self.chartGraphicsView.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        # self.chartGraphicsView.setResizeAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)
        # self.chartGraphicsView.setTransformationAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)

        # BINDING BUTTONS
        self.pb_ChooseImage.clicked.connect(self.open_image_dialog)
        self.pb_RotateLeft.clicked.connect(self.rotate_graphics_view_left)
        self.pb_RotateRight.clicked.connect(self.rotate_graphics_view_right)
        self.pb_DetectReference.clicked.connect(self.detect_reference)
        self.pb_DetectFacialLandmarks.clicked.connect(self.detect_facial_landmarks)
        self.pb_measure.clicked.connect(self.measure)
        # changes from measurement tab automatically tranfer to the chart tab
        self.le_UpperLipMM.textChanged.connect(self.update_growth_chart_le_upper_lip)
        self.le_LeftEyeMM.textChanged.connect(self.update_growth_chart_le_left_eye)
        self.le_RightEyeMM.textChanged.connect(self.update_growth_chart_le_right_eye)
        # self.pb_generate_raport.clicked.connect(self.generate_raport)

        # connecting buttons just in case
        self.pb_chart1.clicked.connect(self.show_diagram_1)
        self.pb_chart2.clicked.connect(self.show_diagram_2)
        self.pb_chart3.clicked.connect(self.show_diagram_3)
        self.pb_chart4.clicked.connect(self.show_diagram_4)
        self.pb_chart5.clicked.connect(self.show_diagram_5)
        self.pb_chart6.clicked.connect(self.show_diagram_6)
        self.pb_chart7.clicked.connect(self.show_diagram_7)
        self.pb_chart8.clicked.connect(self.show_diagram_8)
        self.pb_exportCharts.clicked.connect(self.export_charts)
        self.pb_choose_file.clicked.connect(self.choose_child_file)

    def update_growth_chart_le_upper_lip(self):
        self.le_UpperLipMMChart.setText(self.le_UpperLipMM.text())

    def update_growth_chart_le_left_eye(self):
        self.le_LeftEyeMMChart.setText(self.le_LeftEyeMM.text())

    def update_growth_chart_le_right_eye(self):
        self.le_RightEyeMMChart.setText(self.le_RightEyeMM.text())

    def rotate_graphics_view_right(self):
        self.photoGraphicsView.rotate(90)
        self.rotation += 90
        self.updatePhotoView()

    def rotate_graphics_view_left(self):
        self.photoGraphicsView.rotate(-90)
        self.rotation -= 90
        self.updatePhotoView()

    @qtc.Slot()
    def open_image_dialog(self):
        options = qtw.QFileDialog.Options()
        self.image_path, _ = qtw.QFileDialog.getOpenFileName(self, "Wybierz zdjęcie", "",
                                                             "Obrazy (*.png *.jpg *.jpeg *.bmp)",
                                                             options=options)
        self.updatePhoto()

    def updatePhoto(self):
        load_result = self.backend.load_and_validate(self.image_path)
        if isinstance(load_result, str):
            self.message(load_result, "LightSkyBlue")
        else:
            self.message()
            self.photoScene.clear()
            self.photoScene.clear_canva_state()
            self.image = qtg.QPixmap(self.image_path)
            self.photoScene.addPixmap(self.image)
            self.photoScene.setSceneRect(self.image.rect())
            self.photoScene.update_pen_dimensions()
            self.updatePhotoView()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updatePhotoView()
        # self.updateChartView()

    def updatePhotoView(self):
        self.photoGraphicsView.fitInView(self.photoScene.sceneRect(), qtc.Qt.KeepAspectRatio)

    # def updateChartView(self):
    #     self.chartGraphicsView.fitInView(self.chartScene.sceneRect(), qtc.Qt.KeepAspectRatio)

    def detect_reference(self):
        if self.backend.np_image is None:
            self.message("Nie wybrano obrazu", "LightSkyBlue")
            return
        reference_coords = self.backend.detect_reference()
        if isinstance(reference_coords, str):
            # self.message(reference_coords, "LightSkyBlue")
            self.message("Nie wykryto automatycznie referencji.", "LightSkyBlue")
            self.photoScene.draw_reference(self.placeholder_reference())
        else:
            self.message()
            self.photoScene.draw_reference(reference_coords)

    def placeholder_reference(self):
        width = self.photoScene.width()
        height = self.photoScene.height()

        side_length = width * 0.1
        x1 = width * 0.45
        x2 = min(x1 + side_length, width)
        y1 = height * 0.1
        y2 = min(y1 + side_length, height)
        return [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]

    def message(self, text: str = "", color: str = "white"):
        self.lb_Message.setText(text)
        self.lb_Message.setStyleSheet(f"color: {color}")

    def detect_facial_landmarks(self):
        if self.backend.mp_image is None:
            self.message("Nie wybrano obrazu", "LightSkyBlue")
            return
        facial_landmarks_coords = self.backend.detect_facial_landmarks()
        if isinstance(facial_landmarks_coords, str):
            self.message("Nie wykryto automatycznie twarzy", "LightSkyBlue")
            facial_landmarks_coords = self.placeholder_facial_landmarks()
        else:
            self.message()
        self.photoScene.draw_left_eye(facial_landmarks_coords['left_eye'])
        self.photoScene.draw_right_eye(facial_landmarks_coords['right_eye'])
        self.photoScene.draw_upper_lip(facial_landmarks_coords['upper_lip'])

        # xd = {'left_eye': [[1484.0957736968994, 1487.6388130187988], [1801.3362464904785, 1464.7445755004883]],
        #       'right_eye': [[783.3786163330078, 1473.4267015457153], [1086.4893321990967, 1491.7679557800293]],
        #       'upper_lip': [[1262.3708367347717, 2086.371036529541], [1264.303966999054, 2129.9199571609497]]}

    def placeholder_facial_landmarks(self):
        width = self.photoScene.width()
        height = self.photoScene.height()

        # rotation = self.rotation % 360
        # if rotation==0:
        #     width = self.photoScene.width()
        #     height = self.photoScene.height()
        # if rotation==90:
        #     width = self.photoScene.height()
        #     height = self.photoScene.width()

        eye_y = height * 0.3
        right_eye_x1 = width * 0.1
        right_eye_x2 = width * 0.2
        left_eye_x1 = width * 0.8
        left_eye_x2 = width * 0.9

        lip_x = width * 0.5
        lip_y1 = height * 0.6
        lip_y2 = height * 0.7

        return {'left_eye': [[left_eye_x1, eye_y], [left_eye_x2, eye_y]],
                'right_eye': [[right_eye_x1, eye_y], [right_eye_x2, eye_y]],
                'upper_lip': [[lip_x, lip_y1], [lip_x, lip_y2]]}

    def measure(self):
        if self.not_ready_to_measure():
            self.message(
                "Brakuje danych do pomiarów (referencji, punktów elementów na twarzy lub wielkości referencji w mm",
                "LightSkyBlue"
            )
            return
        self.message()
        facial_landmark_coord_dict = {
            'left_eye': [self.photoScene.left_eye_points[i].get_real_coords() for i in range(2)],
            'right_eye': [self.photoScene.right_eye_points[i].get_real_coords() for i in range(2)],
            'upper_lip': [self.photoScene.lip_points[i].get_real_coords() for i in range(2)]}

        reference_coords = [self.photoScene.reference_points[i].get_real_coords() for i in range(4)]

        ref_in_mm = int(self.le_referenceMM.text())

        results = self.backend.measure(facial_landmark_coord_dict, reference_coords, ref_in_mm)

        self.update_measurement_le(results)

    def not_ready_to_measure(self):
        return (
                len(self.photoScene.lip_points) != 2  # upper lip not detected
                or len(self.photoScene.left_eye_points) != 2  # left eye not detected
                or len(self.photoScene.right_eye_points) != 2  # right eye not detected
                or len(self.photoScene.reference_points) != 4  # reference not detected
                or len(self.le_referenceMM.text()) < 1  # empty reference size
                or int(self.le_referenceMM.text()) < 1  # negative reference size
        )

    def update_measurement_le(self, measurement):
        self.le_LeftEyeMM.setText(str(round(measurement.left_eye, 2)).replace(".", ","))
        self.le_RightEyeMM.setText(str(round(measurement.right_eye, 2)).replace(".", ","))
        self.le_UpperLipMM.setText(str(round(measurement.lip, 2)).replace(".", ","))

    def show_diagram_1(self):
        fig = self.backend.raport_generator.generate_age_eye_width_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['eye_width'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_2(self):
        fig = self.backend.raport_generator.generate_age_eye_width_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['eye_width'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_3(self):
        fig = self.backend.raport_generator.generate_age_upper_lip_height_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['upper_lip'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_4(self):
        fig = self.backend.raport_generator.generate_age_upper_lip_height_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['upper_lip'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_5(self):
        fig = self.backend.raport_generator.generate_age_height_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['height'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_6(self):
        fig = self.backend.raport_generator.generate_age_height_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['height'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_7(self):
        fig = self.backend.raport_generator.generate_age_weight_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['weight'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass

    def show_diagram_8(self):
        fig = self.backend.raport_generator.generate_age_weight_chart()
        if isinstance(fig, str):
            self.message(fig, color="lightskyblue")
            return
        self.generated_charts['weight'] = fig

        # if there is a diagram, then delete it before adding a new one
        if self.diagram:
            self.Siatki_centylowe.layout().removeWidget(self.diagram)

        self.diagram = MplCanvas(fig)
        self.Siatki_centylowe.layout().removeItem(self.the_spacer)
        self.Siatki_centylowe.layout().addWidget(self.diagram)
        pass


    def export_charts(self):
        self.backend.raport_generator.generate(self.generated_charts)
        pass

    def choose_child_file(self):
        self.generated_charts.clear()
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.ReadOnly
        file_path, _ = qtw.QFileDialog.getOpenFileName(self,
                                                       "Wybór pliku z danymi dziecka",
                                                       "",
                                                       "Pliki CSV (*.csv);;Wszystkie pliki (*)",
                                                       options=options)
        if file_path:
            print(file_path)
            self.backend.raport_generator.set_child_data_file(file_path)
            self.message()

    def get_philtrum_depth_class(self):
        if self.rb1.isChecked():
            return 1
        if self.rb2.isChecked():
            return 2
        if self.rb3.isChecked():
            return 3
        if self.rb4.isChecked():
            return 4
        if self.rb5.isChecked():
            return 5
