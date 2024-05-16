import cv2
import math
import os
import tempfile

import numpy as np
from PIL import Image
import pytest
import json
import implementation.processing.measurement_handler as measurement_handler
import mediapipe as mp
from implementation.processing.measurement import Measurement

m_handler = measurement_handler.MeasureHandler()

config = {}
with open("../config.json") as config_file:
    config = json.load(config_file)

correct_measurement_values = config["measurements"]["correct"]
incorrect_measurement_values = config["measurements"]["incorrect"]

correct_cords_values = config["normalized_cords"]["correct"]
incorrect_cords_values = config["normalized_cords"]["incorrect"]
edge_cords_values = config["normalized_cords"]["edge"]

correct_measurement = Measurement(
    correct_measurement_values["left_eye"],
    correct_measurement_values["right_eye"],
    correct_measurement_values["lip"],
)

incorrect_measurement = Measurement(
    correct_measurement_values["left_eye"],
    correct_measurement_values["right_eye"],
    incorrect_measurement_values["lip"],
)


def create_temp_image(width, height):
    temp_image = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with Image.new("RGB", (width, height)) as image:
        image.save(temp_image.name)

    return temp_image.name


def test_calculate_euclidean_distance_px():
    # Test for two points with positive coordinates
    point1 = (1, 2)
    point2 = (4, 6)
    expected_result = math.sqrt((4 - 1) ** 2 + (6 - 2) ** 2)
    assert m_handler.calculate_euclidean_distance_px(point1, point2) == expected_result

    # Test for two points with negative coordinates
    point1 = (-3, -5)
    point2 = (-1, -1)
    expected_result = math.sqrt((-1 - (-3)) ** 2 + (-1 - (-5)) ** 2)
    assert m_handler.calculate_euclidean_distance_px(point1, point2) == expected_result

    # Test for two points with one coordinate being zero
    point1 = (0, 3)
    point2 = (4, 0)
    expected_result = math.sqrt((4 - 0) ** 2 + (0 - 3) ** 2)
    assert m_handler.calculate_euclidean_distance_px(point1, point2) == expected_result

    # Test for two points with both coordinates being zero
    point1 = (0, 0)
    point2 = (0, 0)
    expected_result = 0
    assert m_handler.calculate_euclidean_distance_px(point1, point2) == expected_result


def test_valid_normalized_coordinates():
    result = m_handler.normalized_to_pixel_coordinates(
        correct_cords_values["normalized_x"],
        correct_cords_values["normalized_y"],
        correct_cords_values["image_width"],
        correct_cords_values["image_height"]
    )
    assert result == (50.0, 50.0)


def test_invalid_normalized_coordinates():
    result = m_handler.normalized_to_pixel_coordinates(
        incorrect_cords_values["normalized_x"],
        incorrect_cords_values["normalized_y"],
        incorrect_cords_values["image_width"],
        incorrect_cords_values["image_height"]
    )
    assert result is None


def test_edge_normalized_coordinates():
    result = m_handler.normalized_to_pixel_coordinates(
        edge_cords_values["normalized_x"],
        edge_cords_values["normalized_y"],
        edge_cords_values["image_width"],
        edge_cords_values["image_height"]
    )
    assert result == (0.0, 99.0)


def test_px_to_mm():
    assert m_handler.px_to_mm(9, 17) == 9 * m_handler.reference_in_mm / 17

# def test_validate():
#     try:
#         m_handler.validate(correct_measurement)
#     except measurement_handler.MeasurementsNotCorrect:
#         pytest.fail("Not expected MeasurementNotCorrect exception for correct measurement")
#
#     with pytest.raises(measurement_handler.MeasurementsNotCorrect):
#         m_handler.validate(incorrect_measurement)
#
#
# def test_validate_eye():
#     assert m_handler.validate_eye(25.0)
#     assert not m_handler.validate_eye(0.5)
#     assert not m_handler.validate_eye(51.0)
#
#
# def test_validate_lip():
#     assert m_handler.validate_lip(25.0)
#     assert not m_handler.validate_lip(0.5)
#     assert not m_handler.validate_lip(51.0)
