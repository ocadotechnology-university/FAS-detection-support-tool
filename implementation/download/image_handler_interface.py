from abc import ABC, abstractmethod


class ImageHandlerInterface(ABC):
    @abstractmethod
    def load_image(self, image_path):
        """ Load an image and return it."""
        ...

    @abstractmethod
    def draw_landmarks_on_image(self, rgb_image, detection_result):
        """ Draw landmarks on an image (mediapipe) """
        ...
