from implementation.download.validation.validate_file_content_interface import ValidateFileContentInterface


class FileContentNotValidException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidateFileContent(ValidateFileContentInterface):
    def validate(self, file):
        if not self.is_face_present(file):
            raise FileContentNotValidException("A face was not detected.")

        if not self.is_reference_present(file):
            raise FileContentNotValidException("A reference was not detected.")

    def is_face_present(self, file) -> bool:
        return True

    def is_reference_present(self, file) -> bool:
        return True
