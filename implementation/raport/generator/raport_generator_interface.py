from abc import abstractmethod


class RaportGeneratorInterface:
    """Class for generating raports with centile charts"""

    @abstractmethod
    def generate(self, figures_to_save, file_path):
        """Generates and saves the raport
        """
        ...
