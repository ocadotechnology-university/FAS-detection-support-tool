import implementation.download.validation.validate_file_content
from download.validation.validate_file import FileNotCorrectException
from download.validation.validate_file_content import FileContentNotValidException
from implementation.processing.measurement_handler import MeasurementsNotCorrect

from tools.image import load_image, mediapipe_load_image

import easygui


class Application:
    def __init__(self, measurement_handler, file_validator, file_content_validator):
        self.measurement_handler = measurement_handler
        self.file_validator = file_validator
        self.file_content_validator = file_content_validator

    def run(self):
        # Load path
        file_path = easygui.fileopenbox()
        # Validate file
        try:
            self.file_validator.validate(file_path)
        except FileNotCorrectException as e:
            print("Error in file validation:", e)
            raise
        # Load image
        mp_image = mediapipe_load_image(file_path)
        image = load_image(file_path)
        # Validate image content
        try:
            self.file_content_validator.validate(image, mp_image)
        except FileContentNotValidException as e:
            print("Error in image content validation:", e)
            raise
        # Measure
        measurement_results_px = self.measurement_handler.measure_px(mp_image, show_image=True)
        measurement_results = self.measurement_handler.scale_measurement_with_reference(image, measurement_results_px)
        # Validate measurement
        try:
            self.measurement_handler.validate(measurement_results)
            print(f'right eye = {measurement_results.right_eye}mm')
            print(f'left eye = {measurement_results.left_eye}mm')
            print(f'lip = {measurement_results.lip}mm')
            print(f'philtrum = {measurement_results.philtrum}')
        except MeasurementsNotCorrect:
            # handle exception
            pass
