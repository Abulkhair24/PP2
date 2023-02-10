def ounces(g):
    print("Ounces:", g*28.3495231)
a=int(input())
ounces(a)
def numheadsnumlegs(x, y):
    print("chickens:", ((4*x-y)/2))
    print("rabbits:", ((y-x*2)/2))
h=int(input())
l=int(input())
numheadsnumlegs(h, l)
def celsius(c):
    print("Celsius:", ((5/9)*(f-32)))
f=int(input())
celsius(f)
N=int(input())
numbers = [0]*N
for i in range(N):
    numbers[i]=int(input())
def has33 (nums):
    p=0
    for i in range(N):
        if i<N-1:
            k=i+1
            if nums[i]==nums[k]==3:
                p=+1
    if p==1:
        print(True)
    else:
        print(False)
has33(numbers)
def isPalindrome(str): 
    for i in range(0, len(str)//2+1):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
s=input()
print(isPalindrome(s))
def Guessthenumber():
    p=0
    print("Hello! What is your name?")
    name=input()
    print("Well, " + name + " I am thinking of a number between 1 and 20.")
    print("Take a guess")
    l=int(input())
    while l!=19:
        p=p+1
        print("Your guess is too low.")
        print("Take a guess.")
        l=int(input())
    print("Good job, " + name + " You guessed my number in " + str(p+1) + " guesses!")
Guessthenumber()
s=input()
for i in range(len(s)-1, -1, -1):
    while s[i]!=" ":
        k=+s[i]
print(k)
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])
def toString(List):
    return ''.join(List)
def permute(a, l, r):
    if l == r:
        print (toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
 
            a[l], a[i] = a[i], a[l]
 
string = input()
n = len(string)
a = list(string)
permute(a, 0, n-1)