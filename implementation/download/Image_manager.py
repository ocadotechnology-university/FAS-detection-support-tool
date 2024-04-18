from implementation.download.validation.validate_file import FileNotCorrectException
from implementation.download.validation.validate_file_content import FileContentNotValidException
import mediapipe as mp
# from tkinter import filedialog
import easygui


class ImageManager():
    """a class with one method to load an image into a variable and validate it"""
    def __init__(self, file_validator, file_content_validator):
        self.file_validator = file_validator
        self.file_content_validator = file_content_validator

    def load(self):
        file = easygui.fileopenbox()
        # file = filedialog.askopenfilename()

        if file:
            print("Selected image:", file)
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
            return mp.Image.create_from_file(file)
