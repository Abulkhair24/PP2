import os

path = "/path/to/folder"

dirs_only = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
print("Directories only:", dirs_only)

files_only = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print("Files only:", files_only)

all_contents = os.listdir(path)
print("All contents:", all_contents)