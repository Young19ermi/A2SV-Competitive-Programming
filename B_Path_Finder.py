from collections import defaultdict
n = input()
for _ in range(int(n)):
    graph = defaultdict(list)
    u,v,c = map(int, input().split())

    graph[u].append((v,c))
    graph[v].append((u,c))

    visited= set()
    length = 0
    init = 0
    node = 0

    for x,y in graph[node]:
        if x not in visited:
            length += y
            visited.add(x)
            node = x
            print(x,y)
        else:
            node = init
   
    print(length)