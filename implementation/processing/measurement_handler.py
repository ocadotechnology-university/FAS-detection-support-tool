from interfaces.processing.measurement_handler import MeasureHandlerInterface
from implementation.processing.measurement import Measurement

class MeasurementsNotCorrect(Exception):
    def __init__(self, message):
        super().__init__(message)

class MeasureHandler(MeasureHandlerInterface):
    """Class for performing measure and validate measurement"""
    def measure(self, file):
        measurement = Measurement()
        return measurement

    def validate(self, measurement):
        if not self.validate_eye(measurement.eye):
            raise MeasurementsNotCorrect("Eye measurement is not correct")

        if not self.validate_lip(measurement.eye):
            raise MeasurementsNotCorrect("Lip measurement is not correct")
            
        if not self.validate_philtrum(measurement.eye):
            raise MeasurementsNotCorrect("Philtrum measurement is not correct")

    def validate_eye(self, eye: float) -> bool:
        return True

    def validate_lip(self, lip: float) -> bool:
        return True

    def validate_philtrum(self, philtrum: float) -> bool:
        return True

       

    