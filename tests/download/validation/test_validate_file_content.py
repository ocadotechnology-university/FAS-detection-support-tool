import pytest
import implementation.download.validation.validate_file_content as validate_file_content

v_file_content = validate_file_content.ValidateFileContent()
no_face_photo = "test_photo_no_face.jpg"
no_reference_photo = "test_photo_no_reference.jpg"
correct_photo = "test_correct.jpg"

def test_validate():
    results = [
        v_file_content.validate(no_face_photo),
        v_file_content.validate(no_reference_photo),
        v_file_content.validate(correct_photo)
    ]
    assert results == [False, False, True]


def test_is_face_present():
    results = [
        v_file_content.is_face_present(no_face_photo),
        v_file_content.is_face_present(correct_photo)
    ]
    assert results == [False, True]

def test_is_reference_present():
    results = [
        v_file_content.is_reference_present(no_reference_photo),
        v_file_content.is_reference_present(correct_photo)
    ]
    assert results == [False, True]
