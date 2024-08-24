def solve(nums,a,b):
    nums.sort()
    return nums[int(b)] - nums[int(b)-1]

n,a,b = input().split()
nums = list(map(int, input().split()))
print(solve(nums,a,b))