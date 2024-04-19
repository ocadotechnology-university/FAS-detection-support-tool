from abc import ABC, abstractmethod


class ImageManagerInterface(ABC):
    @abstractmethod
    def load_image(self, file_validator, file_content_validator):
        """ Load and validate image and return it if validation pass"""
        ...

    @abstractmethod
    def draw_landmarks_on_image(self, rgb_image, detection_result):
        """ Draw landmarks on an image (mediapipe) """
        ...
