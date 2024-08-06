m,n = map (int, input().split())
years = 0

while m <= n:
    m = 3 * m
    n = 2*n
    years += 1

print(years)