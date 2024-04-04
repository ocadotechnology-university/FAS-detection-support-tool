import pytest
import implementation.processing.measurement_handler as measurement_handler
from implementation.processing.measurement import Measurement

m_handler = measurement_handler.MeasureHandler()

correct_measurement = Measurement()
correct_measurement.eye = 20.0 # mm
correct_measurement.lip = 15.0 # mm
correct_measurement.philtrum = 3 # type

incorrect_measurement = Measurement()
incorrect_measurement.eye = 10000.0 # mm
incorrect_measurement.lip = 10000.0 # mm
incorrect_measurement.philtrum = 10000 # type

def test_measure():
    correct_file = "test_correct.jpg"
    result = m_handler.measure(correct_file)
    assert isinstance(result, Measurement) == True


def test_validate():
    results = [
        m_handler.validate(correct_measurement),
        m_handler.validate(incorrect_measurement)
    ]
    assert results == [True, False]


def test_validate_eye():
    results = [
        m_handler.validate_eye(1.0),
        m_handler.validate_eye(5.0),
        m_handler.validate_eye(25.0),
        m_handler.validate_eye(625.0)
    ]
    assert results == [False, True, True, False]


def test_validate_lip():
    results = [
        m_handler.validate_lip(1.0),
        m_handler.validate_lip(5.0),
        m_handler.validate_lip(25.0),
        m_handler.validate_lip(625.0)
    ]
    assert results == [True, True, False, False]


def test_validate_philtrum():
    # TODO when philtrum type established
    pass

