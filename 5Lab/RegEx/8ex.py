def split_at_uppercase(string):
    parts = []
    start_index = 0
    for i in range(1, len(string)):
        if string[i].isupper():
            parts.append(string[start_index:i])
            start_index = i
    parts.append(string[start_index:])
    return parts

string = 'SplitThisStringAtUppercaseLetters'
parts = split_at_uppercase(string)

print(parts)