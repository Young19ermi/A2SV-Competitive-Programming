x1, x2, x3 = input().split()
nums = []
nums.append(int(x1))
nums.append(int(x2))
nums.append(int(x3))
nums.sort()
res = 0
mid = nums[1]
print((nums[2]-mid) + (mid - nums[0]))
