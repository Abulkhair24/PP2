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