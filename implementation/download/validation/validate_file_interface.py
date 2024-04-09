from abc import ABC, abstractmethod


class ValidateFileInterface(ABC):
    @abstractmethod
    def validate(self, file):
        """Check if parameters of the file are correct"""
        ...

    @abstractmethod
    def is_file_not_corrupted(self, file) -> bool:
        """Check if file is not corrupted"""
        ...

    @abstractmethod
    def is_file_extension_valid(self, file) -> bool:
        """Check if file extension is valid"""
        ...

    @abstractmethod
    def is_photo_resolution_valid(self, file) -> bool:
        """Check if photo resolution is valid"""
        ...
