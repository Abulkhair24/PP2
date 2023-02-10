def isPalindrome(str): 
    for i in range(0, len(str)//2+1):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
s=input()
print(isPalindrome(s))