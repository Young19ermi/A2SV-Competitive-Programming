def solve(nums,m):
    for i in range(len(nums)-1): 
        if len(nums) != 1:
            if nums[i] <= m:
                nums.remove(nums[i])
            else:
                nums[i] -= m
                k = nums[i]
                nums.append(nums[i])
                nums.remove(nums[i])


        else:
            return nums[0]
n,m = input().split()
nums = list(map(int, input().split()))
print(solve(nums,int(m)))