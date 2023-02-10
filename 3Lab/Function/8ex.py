N=int(input())
numbers = [0]*N
for i in range(N):
    numbers[i]=int(input())
def spy_game (nums):
    K=3
    s=[0]*K
    p=0
    g=0
    for i in range(N):
        if nums[i]==0 or nums[i]==7:
            s[g]=nums[i]
            g=+1
    if s[0]==0 and s[1]==7 and s[2]==0:
        print(True)
    else:
        print(False)
spy_game(numbers)