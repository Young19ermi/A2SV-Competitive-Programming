t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = input()
    b = input()
    r = 0
    for i in range(len(a)):
        if a[:i+1] in b:
            r = max(r, i+1)

    print(r)


    for i in range(len(a)):
        while b[i] != a[i]:
            b.remove(b[i])
            b[i] == b[i+1]
        
