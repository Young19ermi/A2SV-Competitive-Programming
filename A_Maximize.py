from math import * 
def solve(n):
    ans = -100000007
    maxim = 0
    res = 0
    for i in range(1,n):
        if gcd(i,n) + i > res:
            res = gcd(i,n) + i
            maxim = i
    return maxim

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
for _ in range(n):

    for j in range(n):
        nums[i] += nums[j]

        if gcd(i,j) < gcd(i,j) +1