from interfaces.processing.measurement import MeasurementInterface

class Measurement(MeasurementInterface):
    """
    Class for storing results of measure
    -----------------
    Attributes:
        - left/right eye (float): width of an eye
        - lip (float): height of an upper lip
        - philtrum (float): depth of a philtrum
    """
    def __init__(self):
        self.left_eye = 0.0
        self.right_eye = 0.0
        self.lip = 0.0
        self.philtrum = 0.0