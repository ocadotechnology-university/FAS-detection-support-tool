import math

import mediapipe as mp
from mediapipe.tasks import python
from implementation.processing.measurement_handler_interface import MeasureHandlerInterface
from implementation.processing.measurement import Measurement
from implementation.download.image_handler import ImageHandler
import cv2

model_path = "../../resources/face_landmarker.task"


class MeasurementsNotCorrect(Exception):
    def __init__(self, message):
        super().__init__(message)


class MeasureHandler(MeasureHandlerInterface):
    """Class for performing measure and validate measurement"""

    def __init__(self):
        super().__init__()
        base_options = mp.tasks.BaseOptions
        self.face_landmarker = mp.tasks.vision.FaceLandmarker
        face_landmarker_options = mp.tasks.vision.FaceLandmarkerOptions
        vision_running_mode = mp.tasks.vision.RunningMode

        self.options = face_landmarker_options(
            base_options=base_options(model_asset_path=model_path),
            running_mode=vision_running_mode.IMAGE,
            output_facial_transformation_matrixes=True,
            output_face_blendshapes=True,
        )

    def measure(self, image):
        img_handler = ImageHandler()
        with self.face_landmarker.create_from_options(self.options) as landmarker:
            face_landmarker_result = landmarker.detect(image)

        annotated_image = img_handler.draw_landmarks_on_image(image.numpy_view(), face_landmarker_result)
        cv2.imshow('Annotated Image', annotated_image)
        cv2.waitKey(0)  # Wait for any key press
        cv2.destroyAllWindows()  # Close all OpenCV windows
        # Number values of points on face landmark
        point_left_eye_l = 362
        point_left_eye_r = 263
        point_right_eye_l = 33
        point_right_eye_r = 133
        point_upper_lip_up = 0
        point_upper_lip_down = 13

        left_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_left_eye_l].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_left_eye_l].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_left_eye_r].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_left_eye_r].y,
                image_width=image.width,
                image_height=image.height
            ),
        )
        right_eye_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_right_eye_l].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_right_eye_l].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_right_eye_r].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_right_eye_r].y,
                image_width=image.width,
                image_height=image.height
            ),
        )
        lip_size = self.calculate_euclidean_distance_px(
            point1=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_upper_lip_up].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_upper_lip_up].y,
                image_width=image.width,
                image_height=image.height
            ),
            point2=self.normalized_to_pixel_coordinates(
                normalized_x=face_landmarker_result.face_landmarks[0][point_upper_lip_down].x,
                normalized_y=face_landmarker_result.face_landmarks[0][point_upper_lip_down].y,
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


if __name__ == "__main__":
    mh = MeasureHandler()
    measure = mh.measure(mp.Image.create_from_file("../../resources/adult.png"))
    print(measure.left_eye)
    print(measure.right_eye)
    print(measure.lip)
    print(measure.philtrum)
