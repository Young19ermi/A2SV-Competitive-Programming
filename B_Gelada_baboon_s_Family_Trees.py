from collections import defaultdict
n = int(input())
nums = list(map(int, input().split()))
graph = defaultdict(list)


for i in range(len(nums)):
    graph[i].append(nums[i])

t