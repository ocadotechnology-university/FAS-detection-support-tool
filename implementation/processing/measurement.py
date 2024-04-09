from implementation.processing.measurement_interface import MeasurementInterface


class Measurement(MeasurementInterface):
    """
    Class for storing results of measure
    -----------------
    Attributes:
        - eye (float): width of eye
        - lip (float): height of upper lip
        - philtrum (float): depth of philtrum
    """

    def __init__(self):
        self.eye = 0.0
        self.lip = 0.0
        self.philtrum = 0.0
