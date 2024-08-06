class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.experience = [0] * n+1

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            temp = self.parent[x]
            self.parent[x] = root
            x = temp
        return root
    
    def add(k,l):
        k = self.find(k)

    def get(self,u,v):
        return 'YES' if self.find(u) == self.find(v) else 'NO'

    def join(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return
        if rootU != rootV:
            self.parent[rootV] = rootU
        return

n,m = input().split()
for _ in range(int(m)):
    k = input().split(' ')
    if k[0] == 'add':
          print('')













          n, m, k = map(int, input().split())

q = []

p = [i for i in range(100005)]  

def Find(x):
    if p[x] == x:
        return x
    p[x] = Find(p[x])
    return p[x]

def Union(a, b):
    p[Find(b)] = Find(a)  

def solve():
    global q
    ans = []
    for i in range(1, n + 1):
        p[i] = i
    for i in range(k - 1, -1, -1):
        it = q[i]
        s = it[0]
        u = it[1][0]
        v = it[1][1]
        if s == "cut":
            Union(u, v)
        else:
            if Find(u) == Find(v):
                ans.append("YES")
            else:
                ans.append("NO")
    sz = len(ans)
    for i in range(sz - 1, -1, -1):
        print(ans[i])

def input():
    global q
    for i in range(m):
        u, v = map(int, input().split())
    for i in range(k):
        s, u, v = input().split()
        q.append((s, (int(u), int(v))))

solve()


    #####
    

        mini= { i:inf for i in range(1 , n + 1)}
        root = { i:i for i in range(1 , n + 1)}

        def find(x):
            if x == root[x]:
                return x 
            root[x] = find(root[x])
            return root[x]
        
        def union(x , y):
            a = find(x)
            b = find(y)

            if a != b:
                root[a] = b 

        for x , y , dis in roads:
            mini[x] = min(mini[x], dis)
            mini[y] = min(mini[y], dis)
            union(x , y)
        
        for i in range(1, n+1):
            r_i = find(i)
            mini[r_i] = min(mini[r_i], mini[i])


        return mini[find(1)]
