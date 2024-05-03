import os
import sys

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.processing.measurement_handler import MeasureHandler
from implementation.download.image_manager import ImageManager
from application import Application

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    reference_in_mm = int(input("Długość boku referencji w mm")) # this line is temporary, there's  no use validating this user input


    application = Application(
        measurement_handler=MeasureHandler(reference_in_mm),
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
    application.run()


if __name__ == "__main__":
    main()
