import os
import tempfile

import math
import cv2
import mediapipe as mp

from mediapipe.tasks import python

from implementation.processing.measurement_handler_interface import MeasureHandlerInterface
from implementation.processing.measurement import Measurement

from tools.image import draw_landmarks_on_image, get_reference_position, detect_landmarks


class MeasurementsNotCorrect(Exception):
    def __init__(self, message):
        super().__init__(message)


class MeasureHandler(MeasureHandlerInterface):
    """Class for performing measure and validate measurement"""

    # Landmark values of points on face
    LANDMARK_LEFT_EYE_L = 362
    LANDMARK_LEFT_EYE_R = 263
    LANDMARK_RIGHT_EYE_L = 33
    LANDMARK_RIGHT_EYE_R = 133
    LANDMARK_UPPER_LIP_UP = 0
    LANDMARK_UPPER_LIP_DOWN = 13

    def measure(self, image, mp_image, show_image):

        face_landmarker_result = detect_landmarks(mp_image)

        if show_image:
            annotated_image = draw_landmarks_on_image(mp_image.numpy_view(), face_landmarker_result)
            cv2.imshow('Annotated image', annotated_image)
            cv2.waitKey(0)  # Wait for any key press
            cv2.destroyAllWindows()  # Close all OpenCV windows

        # Calibrating using reference
        reference_pos = get_reference_position(image)
        print(f"reference_pos = {reference_pos}")
        # UL UR
        # DL DR
        between_UL_UR = self.calculate_euclidean_distance_px(reference_pos[3], reference_pos[0])
        between_DL_DR = self.calculate_euclidean_distance_px(reference_pos[2], reference_pos[1])
        between_UL_DL = self.calculate_euclidean_distance_px(reference_pos[3], reference_pos[2])
        between_UR_DR = self.calculate_euclidean_distance_px(reference_pos[0], reference_pos[1])

        # Average distance (in pixels) between all reference vertices
        average_dist = (between_UL_UR + between_DL_DR + between_UL_DL + between_UR_DR) / 4
        print(f"average_dist = {average_dist}px")

        left_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
        )
        right_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
        )
        lip_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            ),
        )

        return Measurement(
            # times 10mm divided by average dist in px
            left_eye=left_eye_size * 10 / average_dist,
            right_eye=right_eye_size * 10 / average_dist,
            lip=lip_size * 10 / average_dist,
        )

    def calculate_euclidean_distance_px(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def normalized_to_pixel_coordinates(self,
                                        normalized_x: float,
                                        normalized_y: float,
                                        image_width: int,
                                        image_height: int) -> list[float] | None:

        # Checks if the float value is between 0 and 1.
        def is_valid_normalized_value(value: float) -> bool:
            return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                              math.isclose(1, value))

        if not (is_valid_normalized_value(normalized_x) and
                is_valid_normalized_value(normalized_y)):
            return None

        x_px = float(min(normalized_x * image_width, image_width - 1))
        y_px = float(min(normalized_y * image_width, image_height - 1))

        return [x_px, y_px]

    def validate(self, measurement):
        if not self.validate_eye(measurement.left_eye):
            raise MeasurementsNotCorrect("Left eye measurement is not correct")

        if not self.validate_eye(measurement.right_eye):
            raise MeasurementsNotCorrect("Right eye measurement is not correct")

        if not self.validate_lip(measurement.lip):
            raise MeasurementsNotCorrect("Lip measurement is not correct")

        if not self.validate_philtrum(measurement.philtrum):
            raise MeasurementsNotCorrect("Philtrum measurement is not correct")

    def validate_eye(self, eye: float) -> bool:
        return True

    def validate_lip(self, lip: float) -> bool:
        return True

    def validate_philtrum(self, philtrum: float) -> bool:
        return True
