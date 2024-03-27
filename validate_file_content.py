class FileContentNotCorrectException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidateFileContent:
    def validate(self, file):
        # check if face present
        if not self.is_face_present(file):
            raise FileContentNotCorrectException("File content not valid.")

    def is_face_present(self, file):
        return True