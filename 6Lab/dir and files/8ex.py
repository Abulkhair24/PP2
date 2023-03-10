import os

file_path = "example.txt"

if os.access(file_path, os.F_OK) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted successfully")
else:
    print("File does not exist or cannot be accessed")
