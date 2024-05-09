import sys

import cv2
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.Backend import Backend
from implementation.GUI.w_MainWindow import Ui_w_MainWindow
from PIL import Image


class GUI(qtw.QWidget, Ui_w_MainWindow):
    def __init__(self, backend):
        super().__init__()
        self.setupUi(self)

        self.backend = backend
        self.reference_coords = None

        self.pb_ChooseImage.clicked.connect(self.open_image_dialog)
        self.pb_RotateLeft.clicked.connect(self.rotate_the_image_left)
        self.pb_RotateLeft.clicked.connect(self.rotate_the_image_right)
        self.pb_DetectReference.clicked.connect(self.detect_reference)

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

        self.image_path = None
        self.image = None

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

    def detect_reference(self):
        self.reference_coords = self.backend.detect_reference(self.image_path)
        self.draw_reference()

    def draw_reference(self):
        if self.reference_coords == None:
            return

        for i in range(4):
            next_i = (i + 1) % 4
            x1 = self.reference_coords[i][0]
            y1 = self.reference_coords[i][1]
            x2 = self.reference_coords[next_i][0]
            y2 = self.reference_coords[next_i][1]

            pen = qtg.QPen()
            pen.setColor(qtg.QColor(0xFF0000))
            pen.setWidth(1)
            self.scene.addLine(x1, y1, x2, y2, pen)
