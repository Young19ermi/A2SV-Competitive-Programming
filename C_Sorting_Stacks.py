# def solution(nums):
#     if nums == [0] * length:
#         return 'NO'
#     new = []
#     needed = 0
#     for n in nums:
#         new.append(n-1)
#         needed += 1
    
#     res = []
#     i = 0
#     for n in nums:
#         if needed > 0:
#             prev = n+i
#             res.append(n + i)
#             i += 1
#             needed -= i
#         else:
#             break
#     diff = set(res)
#     if len(diff) != len(nums):
#         return 'NO'
#     return 'YES' if len(res) == len(new) else "NO"
    



# test = int(input())



def solution(nums):
    results = []
    for heights in nums:
        increasing = all(heights[i] < heights[i+1] for i in range(len(heights) - 1))
        if increasing:
            results.append("YES")
        else:
            can_increase = all((heights[i+1] - heights[i]) > 0 for i in range(len(heights) - 1))
            if can_increase:
                results.append("YES")
            else:
                results.append("NO")
    return results

test = int(input())
for _ in range(test):
    length = int(input())
    nums = list(map(int, input().split()))
    print(solution(nums))