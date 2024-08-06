# from itertools import collections
# testcases = int(input())
# for _ in range(testcases):
#     length = input()
#     n = input()
#     numbers =list(map(int, n))
#     prefix_sum = [0] * len(numbers) + 1
#     for i in range(len(numbers)):
#         prefix_sum[i] = prefix_sum[i-1] + numbers[i]
#     hash = collections.defaultdict(int)
#     for j in range(len(prefix_sum)):
from collections import defaultdict
testcases = int(input())
for _ in range(testcases):
    n = int(input())
    a = input()
    d = defaultdict(int)
    d[0] = 1
    res, s = 0, 0
    
    for i in range(n):
        s += int(a[i])
        x = s - i - 1
        d[x] += 1
        
        res += d[x] - 1
        
    print(res)



        # j - i + 1 = prefix_sum[i-1] + numbers[i]











# testcases = int(input())
# for _ in range(testcases):
#     length = input()
#     n = input()
#     numbers =list(map(int, n))
#     count = 0
#     count += numbers.count(1)
#     n =len(numbers)
#     prefix_sum = [0] * (n)
#     prefix_sum[0] = numbers[0] 
#     for i in range(1, n):
#         prefix_sum[i] = prefix_sum[i-1] + numbers[i]
#     i = 0
#     for j in range(len(prefix_sum)):
#         if prefix_sum[j] == j-i+1:
#             count += 1
#     i = 0
#     #for  j in range(len(prefix_sum)):
#     while j < len(prefix_sum):
#         while prefix_sum[j] - prefix_sum[i] == j-i+1:
#             count += 1
#         j += 1
#     i += 1
# #     j = i
# #     print(count)
# testcases = int(input())
# for _ in range(testcases):
#     length = int(input())
#     n = input()
#     numbers = list(map(int, n))
#     count = 0
#     count += numbers.count(1)
#     n = len(numbers)
#     prefix_sum = [0] * (n + 1)
#     for i in range(n):
#         prefix_sum[i + 1] = prefix_sum[i] + numbers[i]
#     total = 0
#     left, right = 0, 0
#     window_sum = 0
#     while right < n:
#         total += numbers[right]
#         if total == right - left + 1:
#             count += 1
#         right += 1
       
#         left += 1

#     print(count+1)


