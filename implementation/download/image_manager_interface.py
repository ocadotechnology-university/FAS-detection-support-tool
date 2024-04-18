from abc import ABC, abstractmethod


class ImageManagerInterface(ABC):
    @abstractmethod
    def load(self, image_path):
        """ Load an image and return it."""
        ...