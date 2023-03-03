def insert_spaces(string):
    new_string = ''
    for i in range(len(string)):
        if string[i].isupper() and i > 0 and string[i-1].islower():
            new_string += ' '
        new_string += string[i]
    return new_string

string = 'InsertSpacesBetweenWordsStartingWithCapitalLetters'
new_string = insert_spaces(string)

print(new_string)