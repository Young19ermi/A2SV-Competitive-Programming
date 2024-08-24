def solve(nums):
    if len(set(nums)) == len(nums):
        nums.sort()
        return (3+nums[0]) * (2+nums[1]) * nums[2]
    
    if len(nums) == 1:
        return (nums[0]+1) * (nums[1]*2) * (nums[2]*3)
    else:
        nums.sort()
        return (nums[0]+5) * (nums[1]) * (nums[2])
n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    print(solve(nums))