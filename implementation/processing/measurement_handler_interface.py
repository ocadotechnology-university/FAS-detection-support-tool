from abc import ABC, abstractmethod
from implementation.processing.measurement import Measurement

class MeasureHandlerInterface(ABC):
    """Class for performing measure and validate measurement"""
    @abstractmethod
    def measure(self, file) -> Measurement:
        """Measure face elements from file"""
        ...

    @abstractmethod
    def validate(self, file):
        """Check if measurements are correct"""
        ...

    @abstractmethod
    def validate_eye(self, eye: float) -> bool:
        """Check if eye measurement is correct"""
        ...

    @abstractmethod
    def validate_lip(self, lip: float) -> bool:
        """Check if lip measurement is correct"""
        ...

    @abstractmethod
    def validate_philtrum(self, philtrum: float) -> bool:
        """Check if philtrum measurement is correct"""
        ...
