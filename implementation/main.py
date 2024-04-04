import sys
import os

# Append the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from download.validation.validate_file import ValidateFile
from download.validation.validate_file import FileNotCorrectException
from download.validation.validate_file_content import ValidateFileContent
from download.validation.validate_file_content import FileContentNotValidException
from implementation.processing.measurement import Measurement
from implementation.processing.measurement_handler import MeasurementsNotCorrect, MeasurementHandler


def main():
    global measurement_results
    file = "photo.png"
    validate_file = ValidateFile()
    validate_file_content = ValidateFileContent()
    measurement_handler = MeasurementHandler()

    try:
        validate_file.validate(file)
        validate_file_content.validate(file)
    except FileNotCorrectException:
        # handle exception
        pass

    try:
        measurement_results = measurement_handler.measure(file)
        measurement_handler.validate(measurement_results)
    except MeasurementsNotCorrect:
        # handle exception
        pass

    print(f'{measurement_results.right_eye=}')
    print(f'{measurement_results.left_eye=}')
    print(f'{measurement_results.philtrum=}')
    print(f'{measurement_results.lip=}')


if __name__ == "__main__":
    main()
