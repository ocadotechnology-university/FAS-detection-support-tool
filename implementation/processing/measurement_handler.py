import os
import math
import cv2
import mediapipe as mp

from mediapipe.tasks import python

from implementation.processing.measurement_handler_interface import MeasureHandlerInterface
from implementation.processing.measurement import Measurement
from implementation.download.image_manager import ImageManager

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../resources/face_landmarker.task")


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
        super().__init__()
        self.face_landmarker = mp.tasks.vision.FaceLandmarker

        # these 3 variables will be used to create self.options
        base_options = mp.tasks.BaseOptions
        face_landmarker_options = mp.tasks.vision.FaceLandmarkerOptions
        vision_running_mode = mp.tasks.vision.RunningMode

        self.options = face_landmarker_options(
            base_options=base_options(model_asset_path=model_path),
            running_mode=vision_running_mode.IMAGE,
            output_facial_transformation_matrixes=True,
            output_face_blendshapes=True,
        )

    def distance(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def get_reference_position(self, image):
        img = cv2.imread(image)
        img_w, img_h, channels = img.shape
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 50, 255, 0)
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
                        img = cv2.drawContours(img, [countour], -1, (0, 255, 0), 2)
                        return approx.reshape(-1, 2).tolist()

    def measure(self, image, show_image):
        img_handler = ImageManager()
        with self.face_landmarker.create_from_options(self.options) as landmarker:
            face_landmarker_result = landmarker.detect(image)

        if show_image:
            annotated_image = img_handler.draw_landmarks_on_image(image.numpy_view(), face_landmarker_result)
            cv2.imshow('Annotated image', annotated_image)
            cv2.waitKey(0)  # Wait for any key press
            cv2.destroyAllWindows()  # Close all OpenCV windows

        # Calibrating using reference
        reference_pos = self.get_reference_position(image)
        # UL UR
        # DL DR
        between_UL_UR = self.distance(reference_pos[3], reference_pos[0])
        between_DL_DR = self.distance(reference_pos[2], reference_pos[1])
        between_UL_DL = self.distance(reference_pos[3], reference_pos[2])
        between_UR_DR = self.distance(reference_pos[0], reference_pos[1])

        # Average distance (in pixels) between all reference vertices
        average_dist = (between_UL_UR + between_DL_DR + between_UL_DL + between_UR_DR)/4

        left_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].y,
                image_width=image.width,
                image_height=image.height
            ),
        )
        right_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_L].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_LEFT_EYE_R].y,
                image_width=image.width,
                image_height=image.height
            ),
        )
        lip_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_UP].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].x,
                normalized_y=face_landmarker_result.face_landmarks[0][self.LANDMARK_UPPER_LIP_DOWN].y,
                image_width=image.width,
                image_height=image.height
            ),
        )

        return Measurement(
            left_eye=left_eye_size,
            right_eye=right_eye_size,
            lip=lip_size,
        )

    def calculate_euclidean_distance_px(self, point1, point2):
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    def normalized_to_pixel_coordinates(self,
                                        normalized_x: float,
                                        normalized_y: float,
                                        image_width: int,
                                        image_height: int) -> tuple[float, float] | None:

        # Checks if the float value is between 0 and 1.
        def is_valid_normalized_value(value: float) -> bool:
            return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                              math.isclose(1, value))

        if not (is_valid_normalized_value(normalized_x) and
                is_valid_normalized_value(normalized_y)):
            return None

        x_px = float(min(normalized_x * image_width, image_width - 1))
        y_px = float(min(normalized_y * image_width, image_height - 1))

        return x_px, y_px

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
