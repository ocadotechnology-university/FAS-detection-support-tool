import json
import math

import implementation.processing.measurement_handler as measurement_handler
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
    assert result == [50.0, 50.0]


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
    assert result == [0.0, 99.0]


def test_calculate_mm_per_px():
    # Set of reference coordinates
    reference_coords = [[0.0, 0.0], [0.0, 100.0], [100.0, 0.0], [100.0, 100.0]]

    # Adjust the coordinates to be 100 pixels apart horizontally/vertically
    reference_coords = [[0.0, 0.0], [0.0, 100.0], [100.0, 100.0], [100.0, 0.0]]

    # Define a reference measurement in millimeters
    reference_in_mm = 100.0

    # Call the method with the defined inputs
    result = m_handler.calculate_mm_per_px(reference_coords, reference_in_mm)

    # The expected result is 1.0, because the average distance between all reference vertices is 100 pixels,
    # and the reference measurement is 100 mm. So, 1 pixel corresponds to 1 mm.
    expected_result = 1.0

    # Check if the output is as expected
    assert math.isclose(result, expected_result, rel_tol=1e-9)


def test_facial_landmarks_in_mm():
    # Define a dictionary of facial landmarks
    facial_landmarks = {
        "left_eye": [[0.0, 0.0], [0.0, 100.0]],
        "right_eye": [[100.0, 0.0], [100.0, 100.0]],
        "upper_lip": [[50.0, 50.0], [50.0, 150.0]]
    }
    # Define a millimeters per pixel ratio
    mm_per_px = 1.0

    # Call the method with the defined inputs
    result = m_handler.facial_landmarks_in_mm(facial_landmarks, mm_per_px)

    # The expected result is a Measurement object with each measurement being 100.0,
    # because the distance between the points of each facial landmark is 100 pixels,
    # and the mm per pixel ratio is 1.0.
    expected_result = Measurement(100.0, 100.0, 100.0)

    # Check if the output is as expected
    assert result == expected_result


def test_get_facial_landmarks_coords():
    pass
