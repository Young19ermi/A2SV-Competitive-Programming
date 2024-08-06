testcase = int(input())
for _ in range(testcase):
    n, h = map(int, input().split())
    count = 0
    for _ in range(n):
        w,l = map(int, input().split())
        count += max(w,l)
    if count >= h:
        print('YES')
    else:
        print('NO')