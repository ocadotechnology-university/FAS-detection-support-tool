import cv2
import math
import os
import tempfile

import numpy as np
from PIL import Image
import pytest
import json
import mediapipe as mp

from tools.image import get_reference_position


def test_get_reference_position():
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (30, 30), (255, 255, 255), -1)
    cv2.imwrite("test_image.png", img)

    reference_position = get_reference_position("test_image.png")
    assert reference_position == [[10, 10], [10, 30], [30, 30], [30, 10]]
