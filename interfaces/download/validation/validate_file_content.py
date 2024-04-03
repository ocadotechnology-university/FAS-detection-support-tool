from abc import ABC, abstractmethod

class ValidateFileContentInterface(ABC):
    @abstractmethod
    def validate(self, file):
        """Check if file content is correct"""
        ...

    @abstractmethod
    def is_face_present(self, file) -> bool:
        """Check if face is present on an image"""
        ...
    
    @abstractmethod
    def is_reference_present(self, file) -> bool:
        """Check if reference is present on an image"""
        ...