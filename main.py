from validate_file import ValidateFile
from validate_file import FileNotCorrectException
from validate_file_content import ValidateFileContent
from validate_file_content import FileContentNotCorrectException
from validate_reference import ValidateReference
from validate_reference import ReferenceNotValidException
from measurements import Measurements
from measurements import MeasurementsNotCorrect

def main():
    file = "photo.png"
    validate_file = ValidateFile()
    validate_file_content = ValidateFileContent()
    validate_reference = ValidateReference()

    try:
        validate_file.validate(file)
        validate_file_content.validate(file)
        validate_reference.validate(file)
    except FileNotCorrectException:
        # handle exception
        pass
    except FileContentNotCorrectException():
        # handle exception
        pass
    except ReferenceNotValidException():
        # handle exception
        pass




if __name__ == "__main__":
    main()