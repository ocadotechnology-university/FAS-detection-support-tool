import math
import cv2

from implementation.processing.measurement_handler_interface import MeasureHandlerInterface
from implementation.processing.measurement import Measurement

from tools.image import  detect_landmarks


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

    def __init__(self):
        pass

    def get_facial_landmarks_coords(self, mp_image):
        face_landmarker_result = detect_landmarks(mp_image)

        facial_landmarks_dict = {}

        facial_landmarks_dict["left_eye"] = [self.normalized_to_pixel_coordinates(
            normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].x,
            normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].y,
            image_width=mp_image.width,
            image_height=mp_image.height
        )
            , self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            )
        ]

        facial_landmarks_dict["right_eye"] = [self.normalized_to_pixel_coordinates(
            normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_RIGHT_EYE_L].x,
            normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_RIGHT_EYE_L].y,
            image_width=mp_image.width,
            image_height=mp_image.height
        )
            , self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_RIGHT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_RIGHT_EYE_R].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            )]

        facial_landmarks_dict["upper_lip"] = [self.normalized_to_pixel_coordinates(
            normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].x,
            normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].y,
            image_width=mp_image.width,
            image_height=mp_image.height),
            self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].y,
                image_width=mp_image.width,
                image_height=mp_image.height
            )]

        return facial_landmarks_dict

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
        y_px = float(min(normalized_y * image_height, image_height - 1))

        return [x_px, y_px]

    def calculate_mm_per_px(self, reference_coords, reference_in_mm):
        # Calibrating using reference
        # UL UR
        # DL DR
        between_UL_UR = self.calculate_euclidean_distance_px(reference_coords[3], reference_coords[0])
        between_DL_DR = self.calculate_euclidean_distance_px(reference_coords[2], reference_coords[1])
        between_UL_DL = self.calculate_euclidean_distance_px(reference_coords[3], reference_coords[2])
        between_UR_DR = self.calculate_euclidean_distance_px(reference_coords[0], reference_coords[1])

        # Average distance (in pixels) between all reference vertices
        average_dist = (between_UL_UR + between_DL_DR + between_UL_DL + between_UR_DR) / 4
        print(f"average_dist = {average_dist}px")
        return reference_in_mm / average_dist

    def facial_landmarks_in_mm(self, facial_landmarks, mm_per_px):
        left_eye_width = self.calculate_euclidean_distance_px(facial_landmarks["left_eye"][0],
                                                              facial_landmarks["left_eye"][1]) * mm_per_px
        right_eye_width = self.calculate_euclidean_distance_px(facial_landmarks["right_eye"][0],
                                                               facial_landmarks["right_eye"][1]) * mm_per_px
        upper_lip_width = self.calculate_euclidean_distance_px(facial_landmarks["upper_lip"][0],
                                                               facial_landmarks["upper_lip"][1]) * mm_per_px
        return Measurement(left_eye_width, right_eye_width, upper_lip_width)


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

