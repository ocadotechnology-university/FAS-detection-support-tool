import sys

import cv2
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from implementation.GUI.w_MainWindow import Ui_w_MainWindow
from PIL import Image


class GUI(qtw.QWidget, Ui_w_MainWindow):
    def __init__(self,         backend):
        super().__init__()
        self.setupUi(self)

        self.backend = backend

        self.pb_ChooseImage.clicked.connect(self.open_image_dialog)
        self.pb_RotateLeft.clicked.connect(self.rotate_the_image_left)
        self.pb_RotateLeft.clicked.connect(self.rotate_the_image_right)

        int_validator = qtg.QIntValidator()
        self.le_referenceMM.setValidator(int_validator)
        self.le_LeftEyeMM.setValidator(int_validator)
        self.le_RightEyeMM.setValidator(int_validator)
        self.le_UpperLipMM.setValidator(int_validator)

        self.scene = qtw.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.graphicsView.setResizeAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.graphicsView.setTransformationAnchor(qtw.QGraphicsView.ViewportAnchor.AnchorViewCenter)

        self.image_path =None
        self.image = None
        self.scene.addLine(0, 0, 30, 30, qtg.QPen(qtg.qRed(255)))

    @qtc.Slot()
    def open_image_dialog(self):
        options = qtw.QFileDialog.Options()
        self.image_path, _ = qtw.QFileDialog.getOpenFileName(self, "Wybierz zdjęcie", "",
                                                             "Obrazy (*.png *.jpg *.jpeg *.bmp)",
                                                             options=options)
        self.updatePhoto()

    def updatePhoto(self):
        self.scene.clear()
        self.image = qtg.QPixmap(self.image_path)
        self.scene.addPixmap(self.image)
        self.scene.setSceneRect(self.image.rect())
        self.updateView()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateView()

    def updateView(self):
        if self.image == None:
            return
        self.graphicsView.fitInView(self.scene.sceneRect(), qtc.Qt.KeepAspectRatio)

    def rotate_the_image_left(self):
        pass
        # img = cv2.imread(self.image_path)
        # rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # cv2.imwrite(self.image_path, rotated_img)
        # self.updatePhoto()


    def rotate_the_image_right(self):
        pass
        # img = cv2.imread(self.image_path)
        # rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        # cv2.imwrite(self.image_path, rotated_img)
        # self.updatePhoto()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())
