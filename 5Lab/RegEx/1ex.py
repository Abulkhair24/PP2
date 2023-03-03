import re
string = input("Enter a string: ")
match = re.search(r'a[b]*', string)
if match:
    print("Match found!")
else:
    print("No match found.")