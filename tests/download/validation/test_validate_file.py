import pytest
import implementation.download.validation.validate_file as validate_file

v_file = validate_file.ValidateFile()
corrupted_file = "test_corrupted.jpg"
correct_file = "test_correct.jpg"
too_big_resolution = "test_too_big.jpg"
too_small_resolution = "test_too_small.jpg"
correct_resolution = "test_correct.jpg"

def test_validate():
    results = [
        v_file.validate(corrupted_file),
        v_file.validate(correct_file),
        v_file.validate(too_small_resolution),
        v_file.validate(too_big_resolution),
        v_file.validate(correct_resolution),
        v_file.validate("photo.exe"),
        v_file.validate("photo.pdf"),
        v_file.validate("photo.jpeg"),
        v_file.validate("photo.jpg"),
        v_file.validate("photo.png")
    ]
    assert results == [False, True, False, False, True, False, False, True, True, True]

def test_is_file_not_corrupted():
    results = [
        v_file.is_file_not_corrupted(corrupted_file),
        v_file.is_file_not_corrupted(correct_file)
    ]
    assert results == [False, True]

def test_is_file_extension_valid():
    results = [
        v_file.is_file_extension_valid("photo.png"),
        v_file.is_file_extension_valid("photo.jpg"),
        v_file.is_file_extension_valid("photo.jpeg"),
        v_file.is_file_extension_valid("photo.pdf"),
        v_file.is_file_extension_valid("photo.exe")
    ]
    assert results == [True, True, True, False, False]


def test_is_photo_resolution_valid():
    results = [
        v_file.is_photo_resolution_valid(too_big_resolution),
        v_file.is_photo_resolution_valid(too_small_resolution),
        v_file.is_photo_resolution_valid(correct_resolution)
    ]
    assert results == [False, False, True]
