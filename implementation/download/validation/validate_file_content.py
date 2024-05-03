from implementation.download.validation.validate_file_content_interface import ValidateFileContentInterface
from tools.image import detect_landmarks, get_reference_position


class FileContentNotValidException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidateFileContent(ValidateFileContentInterface):
    def validate(self, image, mp_image):
        if not self.is_face_present(mp_image):
            raise FileContentNotValidException("A face was not detected.")

        if not self.is_reference_present(image):
            raise FileContentNotValidException("A reference was not detected.")

    def is_face_present(self, image) -> bool:
        result = detect_landmarks(image)
        if result.face_landmarks:
            return True
        return False

    def is_reference_present(self, image) -> bool:
        result = get_reference_position(image)
        if result:
            return True
        return False
