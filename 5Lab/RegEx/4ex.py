import re
pattern = r'[A-Z][a-z]+'
test_string = 'Hello world This is a Test Of Regular Expressions'
matches = re.findall(pattern, test_string)
print(matches)