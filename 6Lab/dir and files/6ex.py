import string

alphabet = string.ascii_uppercase

for letter in alphabet:
    filename = letter + ".txt"
    with open(filename, 'w') as file:
        file.write("This is file " + letter)
