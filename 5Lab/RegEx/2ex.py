import re
pattern = r'a(b{2,3})'
test_string = 'aabbb abc abb bbb'
matches = re.findall(pattern, test_string)
print(matches)