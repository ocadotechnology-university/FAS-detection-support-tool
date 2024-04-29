from abc import ABC, abstractmethod
from implementation.processing.measurement import Measurement


class MeasureHandlerInterface(ABC):
    """Class for performing measure and validate measurement"""

    @abstractmethod
    def get_reference_position(self, file_path):
        """Get position of reference vertices

        Args:
            file_path: path to image (str)

        Returns:
            A list of points [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
        """
        ...

    @abstractmethod
    def measure(self, image, show_image) -> Measurement:
        """Measure size of face elements from image

        Args:
            image: image loaded by mediapipe
            show_image (bool): boolean deciding to show result image or not
        Returns:
            Measurement
        """
        ...

    @abstractmethod
    def calculate_euclidean_distance_px(self, point1, point2) -> float:
        """Calculate Euclidean distance between two points

        Args:
            point1 (tuple[float, float]): First point coordinates in px
            point2 (tuple[float, float]): Second point coordinates in px
        Returns:
            result (float): Euclidean distance in px
        """
        ...

    @abstractmethod
    def normalized_to_pixel_coordinates(self,
                                        normalized_x: float,
                                        normalized_y: float,
                                        image_width: int,
                                        image_height: int) -> tuple[float, float] | None:
        """Converts normalized value pair to pixel coordinates."""
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
