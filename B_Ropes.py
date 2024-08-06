from math import ceil
n,k = map(int, input().split())
nums = []
for _ in range(n):  
    l = int(input())
    nums.append(l)

def solve(p,target):
    res = 0
    for n in p:
        res += n//target
    return res

i = 0
j = max(nums)
precision = 1e-6

res_count = 0
while j-i > precision:
    mid  = (i+j) / 2
 
    if solve(nums,mid) < k:
        j = mid
    else:
        i = mid
print(i) 

# low = 0
# high = max(ropes)
# precision = 1e-6

# while high - low > precision:
#     mid = (low + high) / 2
#     if cuttable_pieces_count(ropes, mid) >= k:
#         low = mid
#     else:
#         high = mid

# print(low)
