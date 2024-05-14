from implementation.download.validation.validate_file_content_interface import ValidateFileContentInterface
from tools.image import detect_landmarks, get_reference_position


class FileContentNotValidException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidateFileContent(ValidateFileContentInterface):

    def validate_face_presence(self, image) -> None:
        result = detect_landmarks(image)
        if not result.face_landmarks:
            raise FileContentNotValidException("Twarz nie została wykryta")

    def validate_reference_presence(self, image) -> None:
        result = get_reference_position(image)
        if not result:
            raise FileContentNotValidException("Referencja nie została wykryta")
