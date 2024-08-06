import string
test1 = list(map(str, input().lower()))
test2 = list(map(str, input().lower()))


if test1 == test2:
    print(str(0))
else:
    nums = list(range(1,27))
    alpha = list(string.ascii_lowercase)
    h = dict(zip(alpha,nums))
    tot1 = 0
    tot2 = 0
    for n in test1:
        tot1 += h[n]

    for n in test2:
        tot2 += h[n]

    if tot1 < tot2:
        print(-1)
    else:
        print(1)