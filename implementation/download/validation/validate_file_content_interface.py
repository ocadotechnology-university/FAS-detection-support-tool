from abc import ABC, abstractmethod


class ValidateFileContentInterface(ABC):
    @abstractmethod
    def validate_face_presence(self, image) -> None:
        """Check if face is present on an image"""
        ...

    @abstractmethod
    def validate_reference_presence(self, image) -> None:
        """Check if reference is present on an image"""
        ...
