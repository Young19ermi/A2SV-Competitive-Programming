def solve(nums):
    res = nums[0]
    for n in nums:
        res &= n
    return res
t = int(input())
for _ in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))