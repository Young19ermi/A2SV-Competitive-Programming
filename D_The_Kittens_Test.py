from collections import defaultdict
class DSU:
    def __init__(self,n):
        self.parent = {i:i for i in range(1, n+1)}
        self.graph = defaultdict(list)

    def find(self,x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp
        return root 

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.graph[x].append(y)
        if len(self.graph[y]) != 0:
           self.graph[x].extend(y)
        return self.graph

    def solve(self,x,y):
        return self.union(x,y)
n = int(input())
solution = DSU(n)

x,y = input().split()
print(solution.solve(int(x),int(y)))