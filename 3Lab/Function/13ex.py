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