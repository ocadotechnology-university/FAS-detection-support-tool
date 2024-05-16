"""Functions used for images"""

import os
import cv2
import mediapipe as mp
import numpy as np

from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks.python.vision.face_landmarker import FaceLandmarkerResult


def load_image(file_path: str) -> np.ndarray:
    """ Load and returns image as ndarray.

    Args:
        file_path (string): Path to image file
    Returns:
        image (ndarray): Image loaded
    """
    return cv2.imread(file_path)


def mediapipe_load_image(file_path: str) -> mp.Image:
    """ Load and returns image as mediapipe image.

        Args:
            file_path (string): Path to image file
        Returns:
            image (mediapipe.Image): Image loaded
        """
    return mp.Image.create_from_file(file_path)


def get_reference_position(img: np.ndarray) -> list[list[float]] | None:
    """Get position of reference vertices

    Args:
        img (ndarray): image file

    Returns:
        A list of points [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] or None if no reference detected
    """
    img_w, img_h, channels = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 100, 255, 0)
    # Find all countours
    contours, _ = cv2.findContours(thresh, 1, 2)

    for countour in contours:
        approx = cv2.approxPolyDP(countour, 0.01 * cv2.arcLength(countour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(countour)
            # Consider only squares with at least 10px of width and height
            if 10 < w < img_w and 10 < h < img_h:
                ratio = float(w) / h
                # Assuming squares have width to height ratio between 0.9 and 1.1
                if 0.9 <= ratio <= 1.1:
                    # img = cv2.drawContours(img, [countour], -1, (0, 255, 0), 2)
                    return approx.reshape(-1, 2).tolist()
    return None


def detect_landmarks(mp_image: mp.Image) -> FaceLandmarkerResult:
    """Detect landmarks in image using mediapipe and returns them in variable

    Args:
        mp_image (mp.Image): image loaded using mediapipe
    Returns:
        landmarks (FaceLandmarkerResult): detected landmarks
    """
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../resources/face_landmarker.task")
    face_landmarker = mp.tasks.vision.FaceLandmarker

    # these 3 variables will be used to create self.options
    base_options = mp.tasks.BaseOptions
    face_landmarker_options = mp.tasks.vision.FaceLandmarkerOptions
    vision_running_mode = mp.tasks.vision.RunningMode

    options = face_landmarker_options(
        base_options=base_options(model_asset_path=model_path),
        running_mode=vision_running_mode.IMAGE,
        output_facial_transformation_matrixes=True,
    )

    with face_landmarker.create_from_options(options) as landmarker:
        face_landmarker_result = landmarker.detect(mp_image)

    return face_landmarker_result


def draw_landmarks_on_image(rgb_image, detection_result):
    """ Draw landmarks on an image (mediapipe)."""
    face_landmarks_list = detection_result.face_landmarks

    # Convert RGB image to BGR format
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)

    # Loop through the detected faces to visualize.
    for idx in range(len(face_landmarks_list)):
        face_landmarks = face_landmarks_list[idx]

        # Draw the face landmarks.
        face_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        face_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in face_landmarks
        ])

        mp.solutions.drawing_utils.draw_landmarks(
            image=bgr_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_RIGHT_EYE,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_contours_style())

        mp.solutions.drawing_utils.draw_landmarks(
            image=bgr_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_LEFT_EYE,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_contours_style())

        mp.solutions.drawing_utils.draw_landmarks(
            image=bgr_image,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_LIPS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles
            .get_default_face_mesh_contours_style())

    return bgr_image
