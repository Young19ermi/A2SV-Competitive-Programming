
class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
    def find(self, x):
        root = x
        
        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp
        return root
        
    def get(self,u,v):
        return 'YES' if self.find(u) == self.find(v) else 'NO'
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            self.parent[rootV] = rootU
        return 
    def g(self, u, v):
        res = self.get(u,v)
        if res:
            return 'YES'
        else:
            return 'NO'
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
        u = int(data[index + 1])
        v = int(data[index + 2])
        results.append(dsu.get(u, v))
        index += 3

for result in results:
    print(result)

def solve(node):
    if node:
        solve(node.left)
        solve(node.right, depth)
        ssolve(node, depth)