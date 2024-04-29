from implementation.download.validation.validate_file import ValidateFile
from implementation.download.validation.validate_file_content import ValidateFileContent
from implementation.processing.measurement_handler import MeasurementsNotCorrect

import easygui
from tkinter import filedialog


class Application:
    def __init__(self, measurement_handler, image_manager):
        self.measurement_handler = measurement_handler
        self.image_manager = image_manager

    def run(self):
        file_path = easygui.fileopenbox()
        # file = filedialog.askopenfilename()

        mp_image = self.image_manager.load_image(
            ValidateFile(10000,
                         100,
                         10000,
                         100,
                         1000,
                         50
                         ),
            ValidateFileContent(),
            file_path
        )

        measurement_results = self.measurement_handler.measure(file_path, mp_image, show_image=True)
        try:
            self.measurement_handler.validate(measurement_results)
            print(f'right eye = {measurement_results.right_eye}mm')
            print(f'left eye = {measurement_results.left_eye}mm')
            print(f'lip = {measurement_results.lip}mm')
            print(f'philtrum = {measurement_results.philtrum}')
        except MeasurementsNotCorrect:
            # handle exception
            pass
