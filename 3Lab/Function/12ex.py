N=int(input())
numbers = [0]*N
for i in range(N):
    numbers[i]=int(input())
def histogram(nums):
    k=len(nums)
    d=k
    g=0
    while k>0:
        while numbers[g]>0:
            print("*")
            numbers[g]=-1
        g=+1
    k=-1
histogram(numbers)