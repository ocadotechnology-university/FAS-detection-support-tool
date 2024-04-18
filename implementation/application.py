import mediapipe as mp

from implementation.download.validation.validate_file import FileNotCorrectException
from implementation.download.validation.validate_file_content import FileContentNotValidException
from implementation.processing.measurement_handler import MeasurementsNotCorrect


class Application:
    def __init__(self, measurement_handler, image_manager):
        self.measurement_handler = measurement_handler
        self.image_manager = image_manager

    def run(self):
        mp_image = self.image_manager.load()
        try:
            measurement_results = self.measurement_handler.measure(mp_image)
            self.measurement_handler.validate(measurement_results)
        except MeasurementsNotCorrect:
            # handle exception
            pass

        print(f'{measurement_results.right_eye=}')
        print(f'{measurement_results.left_eye=}')
        print(f'{measurement_results.philtrum=}')
        print(f'{measurement_results.lip=}')
