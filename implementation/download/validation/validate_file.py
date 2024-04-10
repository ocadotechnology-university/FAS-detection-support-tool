from PIL import Image
from implementation.download.validation.validate_file_interface import ValidateFileInterface


class FileNotCorrectException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ValidateFile(ValidateFileInterface):
    def validate(self, file):
        # check file extension
        if not self.is_file_extension_valid(file):
            raise FileNotCorrectException("File extension not correct.")

        # check if file not corrupted
        if not self.is_file_not_corrupted(file):
            raise FileNotCorrectException("File corrupted.")

        # check photo dimensions
        if not self.is_photo_dimension_valid(file):
            raise FileNotCorrectException("Photo dimension not valid.")

        # check photo resolution
        if not self.is_photo_resolution_valid(file):
            raise FileNotCorrectException("Photo resolution not valid.")

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
        try:
            with Image.open(file) as image:
                # Perform image verification
                image.verify()

                # Close and reload the image (if necessary)
                image.close()

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
                # Checking image dimensions (example conditions)
                if width >= 300 and height >= 300:
                    return True
                else:
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
                    # Checking image resolution (example conditions)
                    if x_dpi >= 72 and y_dpi >= 72:
                        return True
                    else:
                        return False
                else:
                    # If dpi information is not available, consider resolution invalid
                    return False
        except Exception as e:
            print(f"Error checking photo resolution: {str(e)}")
            return False
