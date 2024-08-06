from collections import defaultdict
n = int(input())
graph = defaultdict(list)
u,v,c = map(int, input().split())

graph[u].append((v,c))
graph[v].append((u,c))

visited = set([])
node = 0
for node in graph[neighbour]:
    visited.add(node)
    for node in graph[neighbour]:
        if node not in visited:
            graph[node].append(neighbour)
            graph[node].append(neighbour)


def solve(node, depth):
    if node:
        solve(node.left, depth+1)
        solve(node.right, depth+1)
        graph[depth].append(node.val)

    print(graph)
    solve(graph[0,[0]])
    