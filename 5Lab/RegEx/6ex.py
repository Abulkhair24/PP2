import re

string = 'This is a test string, with some punctuation. It has spaces too.'

new_string = re.sub(r'[ ,.]', ':', string)

print(new_string)