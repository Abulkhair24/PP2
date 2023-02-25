N=int(input())
c = (i**2 for i in range(N+1))
for i in c:
    print(i)
