import sys

import cv2
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.Backend import Backend
from implementation.GUI.Point import Point
from implementation.GUI.Scene import Scene
from implementation.GUI.w_MainWindow import Ui_w_MainWindow
from PIL import Image


class GUI(qtw.QWidget, Ui_w_MainWindow):
    def __init__(self, backend):

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

    def detect_reference(self):
        if self.image_path is None:
            self.message("Nie wybrano obrazu")
            return
        reference_coords = self.backend.detect_reference(self.image_path)

        if reference_coords != None:
            self.scene.draw_reference(reference_coords)
        else:
            self.message("Nie wykryto referencji")

        # TODO funkcja clear_state() po zmianie obrazka

    def message(self, text):
        self.lb_Message.setText(text)

    def detect_facial_landmarks(self):
        facial_landmarks_coords = self.backend.detect_facial_landmarks(self.image_path)
