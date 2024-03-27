class ReferenceNotValidException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ValidateReference:
    def validate(self, file):
        # check if reference present
        if not self.is_reference_present(file):
            raise ReferenceNotValidException("A reference was not detected.")

    def is_reference_present(self, file):
        return True