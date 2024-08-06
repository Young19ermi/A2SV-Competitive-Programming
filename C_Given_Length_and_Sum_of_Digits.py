def can(s,m):
    value = s
    minn = ""

    for i in range(m):
        for d in range(10):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, value - d):
                minn += str(d)
                value -= d
                break

    return minn
m,s = map(int, input().split())
print(can(s,m))


