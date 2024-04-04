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
    # dependency injection
    # now it looks redundant, but as we write more implementations, this abstraction will come in handy
    file_validator_impl = ValidateFile # impl = implementation
    file_content_validator_impl = ValidateFileContent
    measurement_handler_impl = MeasurementHandler

    # proper code
    validate_file = file_validator_impl()
    validate_file_content = file_content_validator_impl()
    measurement_handler = measurement_handler_impl()

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
