from implementation.processing.measurement_interface import MeasurementInterface


class Measurement(MeasurementInterface):
    """
    Class for storing results of measure
    -----------------
    Attributes:
        - left/right eye (float): width of an eye
        - lip (float): height of an upper lip
        - philtrum (float): depth of a philtrum
    """

    def __init__(self,
                 left_eye=0.0,
                 right_eye=0.0,
                 lip=0.0,
                 philtrum=0,
                 ):
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.lip = lip
        self.philtrum = philtrum

    def __eq__(self, other):
        if isinstance(other, Measurement):
            return (self.left_eye == other.left_eye and
                    self.right_eye == other.right_eye and
                    self.lip == other.lip and
                    self.philtrum == other.philtrum)
        return False

    def __str__(self):
        return f"{self.left_eye=}\n \
        {self.right_eye=}\n\
        {self.lip=}\n\
        {self.philtrum=}"