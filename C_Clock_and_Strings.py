n = int(input())
for _ in range(n):
    a,b,c,d = map(int,input().split())

    e = max(a,b)
    f = max(c,d)
    g = min(a,b)
    h = min(c,d)
    # if f > e and (h < g or h in range(f,13)):
    #     print('NO')
    # elif f < e and h > g:
    #     print('NO')
    # else:
    #     print('YES')

    # if c or d in range(min(a,b),max(a,b)+1) and a or b in range(min(c,d),max(c,d)+1):
    #     print('YES')
    # else:
    #     print('NO')

    if min(a,b) in range(min(c,d),max(c,d)+1) and max(c,d) in range(min(a,b),max(a,b)+1):
        print('YES')
    elif min(c,d) in range(min(a,b),max(a,b)+1) and max(a,b) in range(min(c,d),max(c,d)+1):
        print('YES')
    else:
        print('NO')

