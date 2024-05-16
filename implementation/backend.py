import numpy as np
import mediapipe as mp

from download.validation.validate_file import FileNotCorrectException, ValidateFile

from download.validation.validate_file_content import FileContentNotValidException, ValidateFileContent
from implementation.processing.measurement_handler import MeasureHandler

from tools.image import load_image, mediapipe_load_image, get_reference_position



class Backend:
    def __init__(self,
                 measurement_handler: MeasureHandler,
                 file_validator: ValidateFile,
                 file_content_validator: ValidateFileContent):
        self.measurement_handler = measurement_handler
        self.file_validator = file_validator
        self.file_content_validator = file_content_validator
        # two types of images
        self.np_image = None
        self.mp_image = None

    def load_and_validate(self, file_path: str):
        try:
            self.file_validator.validate(file_path)
        except FileNotCorrectException as e:
            return f"Błąd walidacji pliku: {e}"
        # Load image
        self.np_image = load_image(file_path)
        self.mp_image = mediapipe_load_image(file_path)

    def run(self):
        pass
        # Measure
        # measurement_results = self.measurement_handler.scale_measurement_with_reference(image, measurement_results_px)
        # # Validate measurement
        # try:
        #     self.measurement_handler.validate(measurement_results)
        #     print(f'right eye = {measurement_results.right_eye}mm')
        #     print(f'left eye = {measurement_results.left_eye}mm')
        #     print(f'lip = {measurement_results.lip}mm')
        #     print(f'philtrum = {measurement_results.philtrum}')
        # except MeasurementsNotCorrect:
        #     # handle exception
        #     pass

    def detect_reference(self):
        # Validate reference presence
        try:
            self.file_content_validator.validate_reference_presence(self.np_image)
        except FileContentNotValidException as e:
            return f"Błąd walidacji zawartości pliku: {e}"
        reference_pos = get_reference_position(self.np_image)
        return reference_pos

    def detect_facial_landmarks(self):
        # Validate face presence
        try:
            self.file_content_validator.validate_face_presence(self.mp_image)
        except FileContentNotValidException as e:
            return f"Błąd walidacji zawartości pliku: {e}"
        result_dict = self.measurement_handler.get_facial_landmarks_coords(self.mp_image)
        return result_dict

    def measure(self, facial_landmarks_coords, reference_coords, reference_in_mm):
        px_per_mm = self.measurement_handler.calculate_mm_per_px(reference_coords, reference_in_mm)
        result = self.measurement_handler.facial_landmarks_in_mm(facial_landmarks_coords, px_per_mm)
        return result
