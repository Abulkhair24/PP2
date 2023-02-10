def primenumb(k):
    sum_ = 0
    if k == 1:
        sum_+=1
    for p in range(2, k-1, 1):
        if k % p == 0:
            sum_+=1
    if sum_ == 0:
        print(k)
    sum_ = 0
N=int(input())
numbers = [0]*N
for i in range(N):
    numbers[i]=int(input())
for j in range(0, N, 1):
    primenumb(numbers[j])