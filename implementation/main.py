import os
import sys

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.GUI.GUI import GUI
from implementation.processing.measurement_handler import MeasureHandler
from Backend import Backend

import cv2
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from implementation.Backend import Backend
from implementation.GUI.w_MainWindow import Ui_w_MainWindow
from PIL import Image


# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    app = qtw.QApplication(sys.argv)

    ref_in_mm = 23456
    backend = Backend(
        measurement_handler=MeasureHandler(ref_in_mm),
        file_validator=ValidateFile(
            10000,
            100,
            10000,
            100,
            1000,
            50
        ),
        file_content_validator=ValidateFileContent()
    )

    window = GUI(backend)
    window.show()

    sys.exit(app.exec())



if __name__ == "__main__":
    main()
