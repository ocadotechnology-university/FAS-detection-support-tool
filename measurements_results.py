from measurements import Measurements
from measurements import MeasurementsNotCorrect

class MeasurementResults:
    def get_results(self, measurements):
        return measurements.measure()