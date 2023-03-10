filename = "file.txt"
lines = ["line 1", "line 2", "line 3"]

with open(filename, 'w') as file:
    for line in lines:
        file.write(line + "\n")
