from FileFormatValidator import FileFormatValidator
import sys


if __name__ == "__main__":
    validator = FileFormatValidator()
    path = sys.argv[1]
    print(path)
    validator.showMatchingFiles(path, "jpg")

