filename = "file.txt"

with open(filename, 'r') as file:
    num_lines = sum(1 for line in file)
    print("Number of lines:", num_lines)
