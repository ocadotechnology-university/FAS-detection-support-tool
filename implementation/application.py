from implementation.download.validation.validate_file import FileNotCorrectException
from implementation.processing.measurement_handler import MeasurementsNotCorrect


class Application():
    global measurement_results

    def __init__(self, file_validator, file_content_validator, measurement_handler):
        self.file_validator = file_validator
        self.file_content_validator = file_content_validator
        self.measurement_handler = measurement_handler

    def run(self, file):
        global measurement_results

        try:
            self.file_validator.validate(file)
        except FileNotCorrectException:
            # handle exception
            pass

        try:
            self.file_content_validator.validate(file)
        except FileNotCorrectException:
            # handle exception
            pass

        try:
            measurement_results = self.measurement_handler.measure(file)
            self.measurement_handler.validate(measurement_results)
        except MeasurementsNotCorrect:
            # handle exception
            pass

        print(f'{measurement_results.right_eye=}')
        print(f'{measurement_results.left_eye=}')
        print(f'{measurement_results.philtrum=}')
        print(f'{measurement_results.lip=}')
