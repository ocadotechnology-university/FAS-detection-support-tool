from validate_file import ValidateFile
from validate_file import FileNotCorrectException

def main():
    file = "photo.png"
    validate_file = ValidateFile()

    try:
        validate_file.validate(file)
    except FileNotCorrectException as e:
        print("Error bla bla bla")


if __name__ == "__main__":
    main()