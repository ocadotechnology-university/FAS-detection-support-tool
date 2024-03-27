class MeasurementsNotCorrect(Exception):
    def __init__(self, message):
        super().__init__(message)

class Measurements:
    def validate(self, measurement):
        """
        Sprawdzenie czy pomiary sa poprawne
        :param file:
        :return: boolean
        """
        def validate_eye(eye):
            return True

        def validate_lip(lip):
            return True

        def validate_philtrum(philtrum):
            return True

        if validate_eye(measurement.eye) and validate_lip(measurement.lip) and validate_philtrum(measurement.philtrum):
            pass
        else:
            raise MeasurementsNotCorrect("Measurements are invalid")

    def measure(self, file):
        """
        Mierzenie wymiarow twarzy ze zdjecia
        :param file:
        :return: Measurement()
        """
        measurement = Measurement()
        return measurement


class Measurement:
    def __init__(self):
        self.eye = 0
        self.lip = 0
        self.philtrum = 0