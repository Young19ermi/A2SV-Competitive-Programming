from collections import defaultdict,Counter
def solve(n):
    return "".join(n) + "".join(n[::-1])

test = int(input())
for _ in range(test):
    n = input()

    print(solve(n))

from collections simport defaultdict
def solve(n):
    if n not in nums:
        