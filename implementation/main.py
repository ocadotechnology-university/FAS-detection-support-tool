import os
import sys

from download.validation.validate_file import ValidateFile
from download.validation.validate_file_content import ValidateFileContent
from implementation.processing.measurement_handler import MeasureHandler
from application import Application

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    ref_in_mm = int(input("Długość referencji w mm"))
    application = Application(
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
    application.run()


if __name__ == "__main__":
    main()
