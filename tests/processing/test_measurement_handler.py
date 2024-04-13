import tempfile
from PIL import Image
import pytest
import json
import implementation.processing.measurement_handler as measurement_handler
from implementation.processing.measurement import Measurement

m_handler = measurement_handler.MeasureHandler()

config = {}
with open("../config.json") as config_file:
    config = json.load(config_file)

correct_measurement_values = config["measurements"]["correct"]
incorrect_measurement_values = config["measurements"]["incorrect"]

correct_measurement = Measurement()
correct_measurement.eye = correct_measurement_values["eye"]
correct_measurement.lip = correct_measurement_values["lip"]
correct_measurement.philtrum = correct_measurement_values["philtrum"]

incorrect_measurement = Measurement()
incorrect_measurement.eye = incorrect_measurement_values["eye"]
incorrect_measurement.lip = incorrect_measurement_values["lip"]
incorrect_measurement.philtrum = incorrect_measurement_values["philtrum"]

def create_temp_image(width, height):
    temp_image = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with Image.new("RGB", (width, height)) as image:
        image.save(temp_image.name)
    return temp_image.name

def test_measure():
    correct_file = create_temp_image(500, 500)
    result = m_handler.measure(correct_file)
    assert isinstance(result, Measurement) == True


def test_validate():
    try:
        m_handler.validate(correct_measurement)
    except measurement_handler.MeasurementsNotCorrect:
        pytest.fail("Not expected MeasurementNotCorrect exception for correct measurement")

    with pytest.raises(measurement_handler.MeasurementsNotCorrect):
        m_handler.validate(incorrect_measurement)


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

