from abc import ABC, abstractmethod


class ValidateFileContentInterface(ABC):
    @abstractmethod
    def validate(self, image, mp_image):
        """Check if file content is correct"""
        ...

    @abstractmethod
    def is_face_present(self, image) -> bool:
        """Check if face is present on an image"""
        ...

    @abstractmethod
    def is_reference_present(self, image) -> bool:
        """Check if reference is present on an image"""
        ...
