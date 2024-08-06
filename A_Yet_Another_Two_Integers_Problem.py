from math import ceil
n = int(input())

for _ in range(n):
    a,b = map(int, input().split())
    if a < b:
        print(ceil((b-a)/10))
    else:
        print(ceil((a-b)/10))