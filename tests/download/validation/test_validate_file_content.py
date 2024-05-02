import os
import pytest
from implementation.download.validation.validate_file_content import ValidateFileContent
from tools.image import load_image, mediapipe_load_image


@pytest.fixture
def v_file_content():
    return ValidateFileContent()


pth = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

no_face_photo = pth + r"\resources\test_photo_no_face.jpg"
no_reference_photo = pth + r"\resources\test_no_reference.jpg"
correct_photo = pth + r"\resources\test_correct.png"


def test_is_face_present(v_file_content):
    no_face_image = mediapipe_load_image(no_face_photo)
    correct_image = mediapipe_load_image(correct_photo)

    assert v_file_content.is_face_present(no_face_image) == False
    assert v_file_content.is_face_present(correct_image) == True


def test_is_reference_present(v_file_content):
    no_reference_image = load_image(no_reference_photo)
    correct_image = load_image(correct_photo)

    assert v_file_content.is_reference_present(no_reference_image) == False
    assert v_file_content.is_reference_present(correct_image) == True
