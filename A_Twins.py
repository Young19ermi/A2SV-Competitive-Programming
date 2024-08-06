def solve(nums):
    r = 0
    total = sum(nums)
    nums.sort(reverse =True)
    for i in range(len(nums)):
        r += nums[i]
        if r > total - r:
            return i+1

n = int(input())
nums = list(map(int, input().split()))
print(solve(nums))

