def solve(nums):
    initial = nums[0]
    count = 0
    if len(nums) == 2:
        return 1
    for i in range(1,len(nums)):
        if nums[i] >= initial:
            count += 1
            initial = nums[i]
        else:
            initial = nums[i]
    return count
testcase = map(int, input())
nums = list(map(int, input().split()))
print(solve(nums))
