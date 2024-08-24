def solve(nums):
    nums.sort()
    n = len(nums)
    return nums[n//2]
n = int(input())

nums = list(map(int,input().split()))
print(solve(nums))



