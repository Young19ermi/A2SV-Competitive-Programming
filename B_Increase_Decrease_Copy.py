
# def solve(nums,nums2):
#     count = 0
#     if len(nums) == 1:
#         count = 1 + nums2[-1] - nums[0]
#         return count+1
#     if len(set(nums)) == len(set(nums2)):
#         return 1
#     for i in range(len(nums)):
#         if nums2[-1] in range(nums[i], nums2[i]+1):
#             count += nums2[-1]-nums[i] + 1
#             nums[i] = nums[i] + nums2[-1]-nums[i]
    
#     for i in range(len(nums)):
#         count += abs(nums[i] - nums2[i])
#     return count
 
    

# test = int(input())
# for _ in range(test):
#     length = int(input())
#     nums = list(map(int,input().split()))
#     nums2 = list(map(int, input().split()))
#     print(solve(nums,nums2))

import sys

t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    sum_diff = 0
    k = float('inf')
    for i in range(n):
        sum_diff += abs(a[i] - b[i])
        k = min(k, abs(a[i] - b[n]), abs(b[i] - b[n]))
        if min(a[i], b[i]) <= b[n] <= max(a[i], b[i]):
            k = 0
    
    print(sum_diff + k + 1)
    t -= 1

# from sys import stdin

# def I(): return int(stdin.readline().strip())
 
# def II(): return map(int, stdin.readline().strip().split())
 
# def IL(): return list(map(int, stdin.readline().strip().split()))
 
# def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

# def S() : return stdin.readline().strip()

# def SL() : return list(stdin.readline().strip().split())

# from bisect import bisect_left

# def solve():
#     n = I()
#     a = IL()
#     b = IL()

#     last = b.pop()
#     count = 0
#     flag = False

#     for i in range(n):
#         count += abs(a[i] - b[i])
#         if not flag and last in range(a[i], b[i] + 1):
#             count += 1
#             flag = True
    
#     if flag:
#         print(count)
#         return 


#     index = bisect_left(b, last)
#     val = float("inf")
#     if index - 1 >= 0:
#         val = min(val, last - b[index - 1])
    
#     if index + 1 < n:
#         val = min(val, abs(last - b[index + 1]))
    
#     print(val + 1)
 
# T = I()
# for _ in range(T):
#     solve()