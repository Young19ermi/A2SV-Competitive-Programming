import sys

MAX = 200007
MOD = 1000000007

def solve():
    s = input()
    ok = False
    for i in range(1, len(s)):
        if s[i] != s[0]:
            s = s[:i] + s[0] + s[i+1:]
            ok = True
            break
    if not ok:
        print("NO")
        return
    print("YES")
    print(s)

t = int(input())
for _ in range(t):
    solve()

# solve()