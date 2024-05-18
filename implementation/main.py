import os
import sys

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.GUI.gui import GUI
from implementation.processing.measurement_handler import MeasureHandler
from raport.generator.raport_generator import RaportGenerator

from PySide6 import QtWidgets as qtw

from implementation.backend import Backend

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    app = qtw.QApplication(sys.argv)

    backend = Backend(
        measurement_handler=MeasureHandler(),
        file_validator=ValidateFile(
            10000,
            100,
            10000,
            100,
            1000,
            50
        ),
        file_content_validator=ValidateFileContent(),
        raport_generator=RaportGenerator()
    )

    window = GUI(backend)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
