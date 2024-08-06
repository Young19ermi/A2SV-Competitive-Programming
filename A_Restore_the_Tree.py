n,m = map(int, input().split())
indegree = defaultdict(int)
graph = defaultdict(list)
for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
queue = deque()
depth = defaultdict(int)
for key ,items in indegree.items():
    if items == 0:
        count = 0
        queue.append(key, 0)
        depth[key] += count
    

while queue:
    key = queue.popleft()

    for item in graph[key]:
        indegree[item] -= 1
        if indegree[item] == 0:
            queue.append(item)
            