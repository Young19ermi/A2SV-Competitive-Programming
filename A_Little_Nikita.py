def tower(n, m):
    if m <= n and (n % 2 == m % 2):
        return "Yes"
    else:
        return "No"


t = int(input())
results = []


for _ in range(t):
    n, m = map(int, input().split())
    results.append(tower(n, m))

for result in results:
    print(result)