
n = int(input())
m = int(input())
sizes = []
for _ in range(n):
    sizes.append(int(input()))
sizes.sort(reverse=True)
containers = 0
s = 0
for size in sizes:
    if s < m:
        containers += 1
        s += size
print(containers)
