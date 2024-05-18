from abc import abstractmethod


class RaportGeneratorInterface:
    """Class for generating raports with centile charts"""

    @abstractmethod
    def generate(self):
        """Generates and saves the raport
        """
        ...
