class FileNotCorrectException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidateFile:
    def validate(self, file):
        pass

        # check if file not corrupted
        if not self.is_file_corrupted(file):
            raise FileNotCorrectException("File corrupted.")
        # check file extension
        if not self.is_file_extension_valid(file):
            raise FileNotCorrectException("File extension not correct.")
        # check photo resolution
        if not self.is_photo_resolution_valid(file):
            raise FileNotCorrectException("Photo resolution not valid.")

    def is_file_corrupted(self, file):
        return True

    def is_file_extension_valid(self, file):
        return True

    def is_photo_resolution_valid(self, file):
        return True