import mediapipe as mp
from mediapipe.tasks import python
from implementation.processing.measurement_handler_interface import MeasureHandlerInterface
from implementation.processing.measurement import Measurement
from implementation.download.image_handler import ImageHandler
import cv2

model_path = "../resources/face_landmarker.task"


class MeasurementsNotCorrect(Exception):
    def __init__(self, message):
        super().__init__(message)


class MeasureHandler(MeasureHandlerInterface):
    """Class for performing measure and validate measurement"""

    def __init__(self):
        super().__init__()
        self.face_landmarker = mp.tasks.vision.FaceLandmarker

        # these 3 variables will be used to create self.options
        base_options = mp.tasks.BaseOptions
        face_landmarker_options = mp.tasks.vision.FaceLandmarkerOptions
        vision_running_mode = mp.tasks.vision.RunningMode

        self.options = face_landmarker_options(
            base_options=base_options(model_asset_path=model_path),
            running_mode=vision_running_mode.IMAGE)

    def measure(self, file):
        img_handler = ImageHandler()
        with self.face_landmarker.create_from_options(self.options) as landmarker:
            face_landmarker_result = landmarker.detect(file)

        annotated_image = img_handler.draw_landmarks_on_image(file.numpy_view(), face_landmarker_result)
        cv2.imshow('Annotated Image', annotated_image)
        cv2.waitKey(0)  # Wait for any key press
        cv2.destroyAllWindows()  # Close all OpenCV windows
        measurement = Measurement()
        return measurement

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

    # if __name__ == "__main__":
    #     mh = MeasureHandler()
    #     mh.measure(mp.Image.create_from_file("../../resources/adult.png"))
