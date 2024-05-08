from abc import ABC, abstractmethod
from implementation.processing.measurement import Measurement


class MeasureHandlerInterface(ABC):
    """Class for performing measure and validate measurement"""

    @abstractmethod
    def measure_px(self, mp_image, show_image) -> Measurement:
        """Measure size of face elements from image in pixels

        Args:
            mp_image (mp.Image): image loaded by MediaPipe
            show_image (bool): boolean deciding to show result image or not
        Returns:
            Measurement with px values
        """
        ...

    @abstractmethod
    def calculate_euclidean_distance_px(self, point1, point2) -> float:
        """Calculate Euclidean distance between two points

        Args:
            point1 (list[float]): First point coordinates in px
            point2 (list[float]): Second point coordinates in px
        Returns:
            result (float): Euclidean distance in px
        """
        ...

    @abstractmethod
    def normalized_to_pixel_coordinates(self,
                                        normalized_x: float,
                                        normalized_y: float,
                                        image_width: int,
                                        image_height: int) -> tuple[float] | None:
        """Converts normalized value pair to pixel coordinates."""
        ...

    @abstractmethod
    def scale_measurement_with_reference(self, image, measurement: Measurement) -> Measurement:
        """Scale the measurement by a reference size"""
        ...

    @abstractmethod
    def validate(self, file):
        """Check if measurements are correct"""
        ...

    @abstractmethod
    def validate_eye(self, eye: float) -> bool:
        """Check if eye measurement is correct"""
        ...

    @abstractmethod
    def validate_lip(self, lip: float) -> bool:
        """Check if lip measurement is correct"""
        ...

    @abstractmethod
    def validate_philtrum(self, philtrum: float) -> bool:
        """Check if philtrum measurement is correct"""
        ...
