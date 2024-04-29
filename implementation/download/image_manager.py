import cv2

import mediapipe as mp
import numpy as np

from mediapipe.framework.formats import landmark_pb2

from implementation.download.image_manager_interface import ImageManagerInterface
from implementation.download.validation.validate_file import FileNotCorrectException
from implementation.download.validation.validate_file_content import FileContentNotValidException


class ImageManager(ImageManagerInterface):
    """A class for maintaining image operations"""

    def load_image(self, file_validator, file_content_validator, file_path):
        if file_path is None:
            return # no file_path, no worries

        # "there is a file_path" execution branch

        print("Selected image:", file_path)
        try:
            file_validator.validate(file_path)
        except FileNotCorrectException:
            # handle exception
            pass

        try:
            file_content_validator.validate(file_path)
        except FileContentNotValidException:
            # handle exception
            pass
        return mp.Image.create_from_file(file_path)

    def draw_landmarks_on_image(self, rgb_image, detection_result):
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
