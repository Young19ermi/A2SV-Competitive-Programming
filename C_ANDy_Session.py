def solve(z,a):
    mx = 0
    for x in a:
        mx |= x
    ans = mx
    for x in a:
        ans = ans | (x&z)
    return ans

    while z:
        if z > 0:
            z-=1
test = int(input())
for _ in range(test):
    n,z = input().split()
    a = list(map(int,input().split()))
    print(solve(z,a))

    