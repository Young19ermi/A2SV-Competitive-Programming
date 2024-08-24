def solve(nums):
    c = 0
    k = 0
    for i in range(1,len(nums)):
        if nums[i] == '1' and nums[i] == nums[i-1]:
            c += 1
        if nums[i] == '0' and nums[i] == nums[i-1]:
            k += 1
    if c >= 7 or k>=7:
        return 'YES'
    else:
        return 'NO'

nums = input()
nums = list(str(nums))
print(solve(nums))
