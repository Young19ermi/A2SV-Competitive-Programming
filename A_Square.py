from collections import defaultdict
test = int(input())
init = 0
k = 0
side = defaultdict(list)
for _ in range(test):
    x,y = map(int, input().split())
    side[x].append(y)
b = list(set(side.keys()))
print((max(b)-min(b))**2)