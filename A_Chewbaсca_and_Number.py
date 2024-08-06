n = int(input())
nums = list(str(n))
for i in range(len(nums)):
    if i == 0 and int(nums[i]) == 9:
        continue
    elif int(nums[i]) >= 5:
        nums[i] = str(9 - int(nums[i]))
ans = "".join(nums)
print(int(ans))