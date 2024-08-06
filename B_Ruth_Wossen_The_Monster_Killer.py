# n = int(input())

# stones = list(map(int, input().split()))
# queries = input()
# # questions = list(map(int, input().split()))

# prefix_sum = [0] * len(stones)
# prefix_sum[0] = stones[0]

# for i in range(1, len(stones)):
#     prefix_sum[i] = prefix_sum[i-1] + stones[i]
# for _ in range(int(queries)):
#     total = 0
#     type,r,m = map(int, input.split())
#     if type == 1:
#         print(prefix_sum[m] - prefix_sum[r - 1])
        
#     if type == 2:
#         sorted_stones = sorted(stones)
#         sorted_prefix_sum = [0] * len(stones)
#         sorted_prefix_sum[0] = sorted_stones[0]
#         for i in range(1, len(stones)):
#             sorted_prefix_sum[i] = sorted_prefix_sum[i-1] + sorted_stones[i]
#         total += sorted_prefix_sum[m - 1] - sorted_prefix_sum[r - 1]
#         print(total)
n = int(input())
stones = list(map(int, input().split()))
m = int(input())
 
prefix_sum = [0] * (n+1)
 
 
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + stones[i-1]

stones.sort()
prefix = [0] * (n+1)
prefix[0] = stones[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + stones[i]
 
for _ in range(m):
    type, l, r = map(int, input().split())
    if type == 1:
        print(prefix_sum[r] - prefix_sum[l-1])
    else:
        
        print(prefix[r-1] - prefix[l-2])