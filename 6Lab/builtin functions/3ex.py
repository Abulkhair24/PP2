def is_palindrome(string):
    return string == string[::-1]

string = "racecar"
if is_palindrome(string):
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")