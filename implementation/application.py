from implementation.download.validation.validate_file import FileNotCorrectException
from implementation.download.validation.validate_file_content import FileContentNotValidException
from implementation.processing.measurement_handler import MeasurementsNotCorrect


class Application:
    def __init__(self, image_handler, file_validator, file_content_validator, measurement_handler):
        self.image_handler = image_handler
        self.file_validator = file_validator
        self.file_content_validator = file_content_validator
        self.measurement_handler = measurement_handler

    def run(self, file):
        try:
            self.file_validator.validate(file)
        except FileNotCorrectException:
            # handle exception
            pass

        try:
            self.file_content_validator.validate(file)
        except FileContentNotValidException:
            # handle exception
            pass

        img = self.image_handler.load_image(file)

        try:
            measurement_results = self.measurement_handler.measure(img, show_image=True)
            self.measurement_handler.validate(measurement_results)
            print(f'right eye = {measurement_results.right_eye}px')
            print(f'left eye = {measurement_results.left_eye}px')
            print(f'lip = {measurement_results.lip}px')
            print(f'philtrum = {measurement_results.philtrum}')
        except MeasurementsNotCorrect:
            # handle exception
            pass
