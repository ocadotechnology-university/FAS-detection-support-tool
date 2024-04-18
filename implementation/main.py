import os
import sys

from implementation.download.Image_manager import ImageManager

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.processing.measurement_handler import MeasureHandler
from application import Application


def main():
    application = Application(
        MeasureHandler(),
        ImageManager(
            ValidateFile(10000, 100, 10000, 100, 1000, 50),
            ValidateFileContent()))
    application.run()


if __name__ == "__main__":
    main()
