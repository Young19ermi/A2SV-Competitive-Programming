from math import * 
test = int(input())
for _ in range(test):
    num = int(input())
    k = log(num, 2)
    print(k)
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            return True
return False


for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            return 0
for k in range(len(nums)):
    while i < len(nums):
        if nums[j] =