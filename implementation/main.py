import os
import sys

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.processing.measurement_handler import MeasureHandler
from application import Application


def main():
    file = "photo.png"
    application = Application(ValidateFile(), ValidateFileContent(), MeasureHandler())
    application.run(file)


if __name__ == "__main__":
    main()
