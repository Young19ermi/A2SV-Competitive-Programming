import sys
ipnput = sys.stdin.readline

def solve(n,z,a):
    mx = 0
    for x in a:
        mx |= x
    ans = mx
    for x in a:
        ans = ans | (x&z)
    return ans

t = int(input())
for _ in range(t):
    n,z = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n,z,a))