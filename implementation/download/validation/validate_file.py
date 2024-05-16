import os
from PIL import Image
from implementation.download.validation.validate_file_interface import ValidateFileInterface


class FileNotCorrectException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidateFile(ValidateFileInterface):
    def __init__(self, max_width, min_width, max_height, min_height, max_dpi, min_dpi):
        """
        Constructor for ValidateFile class.

        Args:
            max_width (int): Maximum width of the image.
            min_width (int): Minimum width of the image.
            max_height (int): Maximum height of the image.
            min_height (int): Minimum height of the image.
            max_dpi (int): Maximum DPI (dots per inch) of the image.
            min_dpi (int): Minimum DPI (dots per inch) of the image.
        """
        self.max_width = max_width
        self.min_width = min_width
        self.max_height = max_height
        self.min_height = min_height
        self.max_dpi = max_dpi
        self.min_dpi = min_dpi

    def validate(self, file):
        """
        Check if parameters of the file are correct

        Args:
            file (str): Path to the image file.

        Raises:
            FileNotCorrectException: If the file parameters are not correct.

        Returns:
            None
        """
        # Check if the file exists
        if not os.path.exists(file):
            raise FileNotCorrectException(f"Plik {file} nie istnieje.")

        # Check if the path is a file
        if not os.path.isfile(file):
            raise FileNotCorrectException(f"{file} nie jest plikiem.")

        # Check if the file is readable
        if not os.access(file, os.R_OK):
            raise FileNotCorrectException(f"Plik {file} nie ma prawa do odczytu.")

        # check file extension
        if not self.is_file_extension_valid(file):
            raise FileNotCorrectException("Rozszerzenie pliku jest niepoprawne")

        # check if file not corrupted
        if not self.is_file_not_corrupted(file):
            raise FileNotCorrectException("Plik uszkodzony")

        # check photo dimensions
        if not self.is_photo_dimension_valid(file):
            raise FileNotCorrectException("Wymiary zdjęcia są niepoprawne")

        # check photo resolution
        # if not self.is_photo_resolution_valid(file):
        #     raise FileNotCorrectException("Photo resolution not valid.")

    def is_file_extension_valid(self, file) -> bool:
        """
        Check if the file has a valid image extension.

        Args:
            file (str): Path to the image file.

        Returns:
            bool: True if the file extension is valid, False otherwise.
        """
        valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        try:
            return any(file.lower().endswith(ext) for ext in valid_extensions)
        except Exception as e:
            print(f"Error checking file extension: {str(e)}")
            return False

    def is_file_not_corrupted(self, file) -> bool:
        """
        Check if the image file is not corrupted.

        Args:
            file (str): Path to the image file.

        Returns:
            bool: True if the image file is not corrupted, False otherwise.
        """

        try:
            with Image.open(file) as image:
                # Perform image verification
                image.verify()

                # Close and reload the image (if necessary)
                # image.close()

                # Re-open the image (if necessary) to perform additional operations
                with Image.open(file) as img:
                    # Try to apply an operation on the image (transposing)
                    img.transpose(Image.FLIP_LEFT_RIGHT)
            return True
        except Exception as e:
            print(f"Error checking file corruption: {str(e)}")
            return False

    def is_photo_dimension_valid(self, file) -> bool:
        """
        Check if the dimensions of the image file are valid.

        Args:
            file (str): Path to the image file.

        Returns:
            bool: True if the image dimensions are valid, False otherwise.
        """
        try:
            with Image.open(file) as image:
                width, height = image.size
                if self.min_width < width < self.max_width and self.min_height < height < self.max_height:
                    return True
                return False
        except Exception as e:
            print(f"Error checking photo dimensions: {str(e)}")
            return False

    def is_photo_resolution_valid(self, file) -> bool:
        """
        Check if the resolution of the image file is valid.

        Args:
            file (str): Path to the image file.

        Returns:
            bool: True if the image resolution is valid, False otherwise.
        """
        try:
            with Image.open(file) as image:
                # Check if the image contains dpi resolution information
                if image.info.get('dpi'):
                    x_dpi, y_dpi = image.info['dpi']
                    # Check if dpi resolutions are consistent
                    if x_dpi != y_dpi:
                        print('Inconsistent DPI image data')
                        return False
                    if x_dpi < self.min_dpi:
                        return False
                    if x_dpi > self.max_dpi:
                        return False
                    return True
                else:
                    # If dpi information is not available, consider resolution invalid
                    return False
        except Exception as e:
            print(f"Error checking photo resolution: {str(e)}")
            return False
