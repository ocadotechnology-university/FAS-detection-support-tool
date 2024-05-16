import cv2
import tempfile
import numpy as np
import mediapipe as mp

import os
import tools.image as image_tools


def test_get_reference_position():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (30, 30), (255, 255, 255), -1)
    cv2.imwrite("test_image.png", img)

    loaded_image = image_tools.load_image("test_image.png")
    reference_position = image_tools.get_reference_position(loaded_image)

    assert reference_position == [[10, 10], [10, 30], [30, 30], [30, 10]]


def test_load_image():
    # Create a temporary image file
    temp_image_file = tempfile.NamedTemporaryFile(suffix=".png").name
    cv2.imwrite(temp_image_file, np.zeros((100, 100, 3), np.uint8))

    # Load the image using the function
    loaded_image = image_tools.load_image(temp_image_file)

    # Check that the returned object is a numpy array
    assert isinstance(loaded_image, np.ndarray)

    # Remove the temporary image file
    os.remove(temp_image_file)


def test_mediapipe_load_image():
    # Create a temporary image file
    temp_image_file = tempfile.NamedTemporaryFile(suffix=".png").name
    cv2.imwrite(temp_image_file, np.zeros((100, 100, 3), np.uint8))

    # Load the image using the function
    loaded_image = image_tools.mediapipe_load_image(temp_image_file)

    # Check that the returned object is a mediapipe Image
    assert isinstance(loaded_image, mp.Image)

    # Remove the temporary image file
    os.remove(temp_image_file)
