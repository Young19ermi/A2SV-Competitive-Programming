def solve(n,k):
    a,b = divmod(n,k)
    if b:
        a += 1
    return (k*a + n-1 )// n

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    print(solve(n,k))