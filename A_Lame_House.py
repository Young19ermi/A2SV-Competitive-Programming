def solve():
    y = input()
    fir = int(y[0]) -1
    l = len(y)
    res = fir * 10 + l * (l+1)//2
    return res
t = int(input())
for _ in range(t):
    print(solve())