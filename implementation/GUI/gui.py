from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.GUI.scene import Scene
from implementation.GUI.w_main_window import Ui_w_MainWindow
from implementation.backend import Backend


class GUI(qtw.QWidget, Ui_w_MainWindow):
    def __init__(self, backend: Backend):

        # startup
        super().__init__()
        self.setupUi(self)

        # backend and state
        self.backend = backend
        self.reference_points = []
        self.image_path = None

        # things in the graphics area
        self.image = None  # qtg.QPixmap

        # VALIDATING INPUT
        int_validator = qtg.QIntValidator()
        self.le_referenceMM.setValidator(int_validator)
        self.le_LeftEyeMM.setValidator(int_validator)
        self.le_RightEyeMM.setValidator(int_validator)
        self.le_UpperLipMM.setValidator(int_validator)

        # Scene Creation
        self.scene = Scene()
        self.graphicsView.setScene(self.scene)

        # making sure that the scene is always in the center off graphicsview
        self.graphicsView.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.graphicsView.setResizeAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.graphicsView.setTransformationAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)

        # BINDING BUTTONS
        self.pb_ChooseImage.clicked.connect(self.open_image_dialog)
        self.pb_RotateLeft.clicked.connect(self.scene.rotate_the_image_left)
        self.pb_RotateLeft.clicked.connect(self.scene.rotate_the_image_right)
        self.pb_DetectReference.clicked.connect(self.detect_reference)
        self.pb_DetectFacialLandmarks.clicked.connect(self.detect_facial_landmarks)
        self.pb_measure.clicked.connect(self.measure)
        self.pb_generate_raport.clicked.connect(self.generate_raport)

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
            self.message(load_result, "red")
        else:
            self.message()
            self.scene.clear()
            self.scene.clear_canva_state()
            self.image = qtg.QPixmap(self.image_path)
            self.scene.addPixmap(self.image)
            self.scene.setSceneRect(self.image.rect())
            self.updateView()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateView()

    def updateView(self):
        if self.image is None:
            return
        self.graphicsView.fitInView(self.scene.sceneRect(), qtc.Qt.KeepAspectRatio)

    def detect_reference(self):
        if self.backend.np_image is None:
            self.message("Nie wybrano obrazu", "red")
            return
        reference_coords = self.backend.detect_reference()
        if isinstance(reference_coords, str):
            self.message(reference_coords, "red")
        else:
            self.message()
            self.scene.draw_reference(reference_coords)

    def message(self, text: str = "", color: str = "white"):
        self.lb_Message.setText(text)
        self.lb_Message.setStyleSheet(f"color: {color}")

    def detect_facial_landmarks(self):
        if self.backend.mp_image is None:
            self.message("Nie wybrano obrazu", "red")
            return
        facial_landmarks_coords = self.backend.detect_facial_landmarks()
        if isinstance(facial_landmarks_coords, str):
            self.message(facial_landmarks_coords, "red")
        else:
            self.message()
            self.scene.draw_left_eye(facial_landmarks_coords['left_eye'])
            self.scene.draw_right_eye(facial_landmarks_coords['right_eye'])
            self.scene.draw_upper_lip(facial_landmarks_coords['upper_lip'])

        # xd = {'left_eye': [[1484.0957736968994, 1487.6388130187988], [1801.3362464904785, 1464.7445755004883]],
        #       'right_eye': [[783.3786163330078, 1473.4267015457153], [1086.4893321990967, 1491.7679557800293]],
        #       'upper_lip': [[1262.3708367347717, 2086.371036529541], [1264.303966999054, 2129.9199571609497]]}

    def measure(self):
        if self.not_ready_to_measure():
            self.message(
                "Brakuje danych do pomiarów (referencji, punktów elementów na twarzy lub wielkości referencji w mm",
                "red"
            )
            return
        self.message()
        facial_landmark_coord_dict = {'left_eye': [self.scene.left_eye_points[i].get_real_coords() for i in range(2)],
                                      'right_eye': [self.scene.right_eye_points[i].get_real_coords() for i in range(2)],
                                      'upper_lip': [self.scene.lip_points[i].get_real_coords() for i in range(2)]}

        reference_coords = [self.scene.reference_points[i].get_real_coords() for i in range(4)]

        ref_in_mm = int(self.le_referenceMM.text())

        results = self.backend.measure(facial_landmark_coord_dict, reference_coords, ref_in_mm)

        self.update_measurement_le(results)

    def not_ready_to_measure(self):
        return (
                len(self.scene.lip_points) != 2             # upper lip not detected
                or len(self.scene.left_eye_points) != 2     # left eye not detected
                or len(self.scene.right_eye_points) != 2    # right eye not detected
                or len(self.scene.reference_points) != 4    # reference not detected
                or len(self.le_referenceMM.text()) < 1      # empty reference size
                or int(self.le_referenceMM.text()) < 1      # negative reference size
        )

    def update_measurement_le(self, measurement):
        self.le_LeftEyeMM.setText(str(round(measurement.left_eye, 2)))
        self.le_RightEyeMM.setText(str(round(measurement.right_eye, 2)))
        self.le_UpperLipMM.setText(str(round(measurement.lip, 2)))

    def generate_raport(self):
        self.backend.generate_raport()
