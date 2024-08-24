def solve(nums):
    res = []
    i  = 0
    while i < len(nums)-1:
        res.append(nums[i]+nums[i+1])
        i+=1
    res.append(nums[-1])
    return res
n = int(input())
nums = list(map(int, input().split()))
print(*solve(nums))