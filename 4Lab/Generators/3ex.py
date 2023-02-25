def func(d):
    c = (i**2 for i in range(d+1))
    for i in c:
        print(i)
N = int(input())
func(N)