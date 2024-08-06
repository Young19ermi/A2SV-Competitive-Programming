def solve(n):
    c,k = 0,0
    while c <= n:
        k += 1
        c += k *(k+1)//2
    print(k-1)
n = int(input())
solve(n)