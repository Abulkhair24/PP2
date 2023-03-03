import re

pattern = r'a.*b$'

test_string = 'a test string that ends in b'

match = re.search(pattern, test_string)

if match:
    print(match.group())
else:
    print('No match found.')