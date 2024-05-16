from abc import ABC, abstractmethod
from implementation.processing.measurement import Measurement


class MeasureHandlerInterface(ABC):
    """Class for performing measure and validate measurement"""

    @abstractmethod
    def calculate_euclidean_distance_px(self, point1: list[float], point2: list[float]) -> float:
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
                                        image_height: int) -> list[float] | None:
        """Converts normalized value pair to pixel coordinates.
        Args:
            normalized_x (float): Normalized x coordinate
            normalized_y (float): Normalized y coordinate
            image_width (int): Width of the image
            image_height (int): Height of the image
        Returns:
            result (list[float] | None): Pixel coordinates or None if normalized values are invalid
        """
        ...

    @abstractmethod
    def get_facial_landmarks_coords(self, mp_image) -> dict:
        """Get facial landmarks coordinates
        Args:
            mp_image: The image to get facial landmarks from
        Returns:
            facial_landmarks_dict (dict): A dictionary with facial landmarks coordinates
        """
        ...

    @abstractmethod
    def calculate_mm_per_px(self, reference_coords: list[list[float]], reference_in_mm: float) -> float:
        """Calculate millimeters per pixel
        Args:
            reference_coords (list[list[float]]): The reference coordinates
            reference_in_mm (float): The reference in millimeters
        Returns:
            mm_per_px (float): The number of millimeters per pixel
        """
        ...

    @abstractmethod
    def facial_landmarks_in_mm(self, facial_landmarks: dict, mm_per_px: float) -> Measurement:
        """Convert facial landmarks to millimeters
        Args:
            facial_landmarks (dict): The facial landmarks coordinates
            mm_per_px (float): The number of millimeters per pixel
        Returns:
            measurement (Measurement): The measurement of facial landmarks in millimeters
        """
        ...
