import tempfile
import pytest
import os
from PIL import Image
import json
import implementation.download.validation.validate_file as validate_file

config = {}
with open("../../config.json") as config_file:
    config = json.load(config_file)

valid_extensions = config["valid_extensions"]
invalid_extensions = config["invalid_extensions"]
max_width = config["max_width"]
min_width = config["min_width"]
max_height = config["max_height"]
min_height = config["min_height"]
max_dpi = config["max_dpi"]
min_dpi = config["min_dpi"]

v_file = validate_file.ValidateFile(max_width, min_width, max_height, min_height, max_dpi, min_dpi)


def create_temp_image(width, height):
    temp_image = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with Image.new("RGB", (width, height)) as image:
        image.save(temp_image.name)
    return temp_image.name


def create_temp_image_with_resolution(dpi):
    width_inch = 1
    height_inch = 1
    width = width_inch * dpi
    height = height_inch * dpi

    temp_image = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with Image.new("RGB", (width, height)) as image:
        image.save(temp_image.name, dpi=(dpi, dpi))
    return temp_image.name


def create_corrupted_image():
    temp_image = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with open(temp_image.name, "wb") as file:
        file.write(b"not image data")
    return temp_image.name


correct_file = create_temp_image(300, 300)
corrupted_file = create_corrupted_image()

v_file.min_width = min_width
v_file.max_width = max_width
v_file.min_height = min_height
v_file.max_height = max_height

valid_image = create_temp_image(200, 200)
too_small_image = create_temp_image(50, 50)
too_big_image = create_temp_image(600, 600)

v_file.min_dpi = min_dpi
v_file.max_dpi = max_dpi
valid_image_res = create_temp_image_with_resolution(150)
too_small_image_res = create_temp_image_with_resolution(30)
too_big_image_res = create_temp_image_with_resolution(500)


def test_validate():
    with pytest.raises(validate_file.FileNotCorrectException):
        v_file.validate(corrupted_file)

    with pytest.raises(validate_file.FileNotCorrectException):
        v_file.validate(too_small_image)

    with pytest.raises(validate_file.FileNotCorrectException):
        v_file.validate(too_big_image)

    with pytest.raises(validate_file.FileNotCorrectException):
        v_file.validate(too_small_image_res)

    with pytest.raises(validate_file.FileNotCorrectException):
        v_file.validate(too_big_image_res)


def test_is_file_not_corrupted():
    results = [
        v_file.is_file_not_corrupted(corrupted_file),
        v_file.is_file_not_corrupted(correct_file)
    ]
    assert results == [False, True]


def test_is_file_extension_valid():
    expected_results = []
    actual_results = []
    for valid in valid_extensions:
        actual_results.append(v_file.is_file_extension_valid(f"photo.{valid}"))
        expected_results.append(True)
    for invalid in invalid_extensions:
        actual_results.append(v_file.is_file_extension_valid(f"photo.{invalid}"))
        expected_results.append(False)

    assert expected_results == actual_results


def test_is_photo_dimension_valid():
    assert v_file.is_photo_dimension_valid(valid_image) == True
    assert v_file.is_photo_dimension_valid(too_small_image) == False
    assert v_file.is_photo_dimension_valid(too_big_image) == False

    os.unlink(valid_image)
    os.unlink(too_small_image)
    os.unlink(too_big_image)


def test_is_photo_resolution_valid():
    assert v_file.is_photo_resolution_valid(valid_image_res) == True
    assert v_file.is_photo_resolution_valid(too_small_image_res) == False
    assert v_file.is_photo_resolution_valid(too_big_image_res) == False

    os.unlink(valid_image_res)
    os.unlink(too_small_image_res)
    os.unlink(too_big_image_res)
