def solve(k,m,a,b):
    a.sort()
    b.sort()
    selecteda = a[0:k+1]

    for i in range(len(k)):
        selecteda.append()
    for i in range(len(k)):



n,m = int(input().split())
k,m = int(input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(k,m,a,b))
