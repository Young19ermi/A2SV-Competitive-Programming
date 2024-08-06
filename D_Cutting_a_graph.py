class DSU:
    def __init__(self,n):
        self.parent = {i:i for i in range(1, n+1)}
        self.size = [1] * (n+1)
        self.res = []
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
        
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        return 

    def ask(self,x,y):
    
        if self.find(x) == self.find(y):
            self.res.append('YES')
        else:
            self.res.append('NO')

    def solve(self,cmd,x,y):

        if cmd == 'ask':
            self.ask(x,y)
        else:
            self.union(x,y)
    
n,m,k = input().split()
command = []
for _ in range(int(m)):
    u,v = input().split()

solution = DSU(int(n))
for _ in range(int(k)):
    cmd,u,v = input().split()
    command.append([cmd,int(u),int(v)])

for cmd, u, v in reversed(command):
    solution.solve(cmd,u,v)

for i in reversed(solution.res):
    print(i)
    
