class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
        self.min = list(range(n+1))
        self.max = list(range(n+1))
        self.size = [1] * (n+1)
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                rootU, rootV = rootV, rootU  
            if self.rank[rootU] == self.rank[rootV]:
                self.rank[rootV] += 1
            self.parent[rootU] = rootV
            self.size[rootV] += self.size[rootU]
            self.min[rootV] = min(self.min[rootV], self.min[rootU])
            self.max[rootV] = max(self.max[rootV], self.max[rootU])

    def get(self, v):
        root = self.find(v)
        return (self.min[root], self.max[root], self.size[root])


import sys
input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
dsu = DSU(n)
index = 2

results = []
for _ in range(m):
    command = data[index]
    if command == 'union':
        u = int(data[index + 1])
        v = int(data[index + 2])
        dsu.union(u, v)
        index += 3
    elif command == 'get':
        v = int(data[index + 1])
        results.append(dsu.get(v))
        index += 2

for result in results:
    print(*result)