n,m = map(int, input().split())
nums = list(range(0,1000))
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] ** 2 + nums[j] == n and nums[i] + nums[j] ** 2 == m:
            count += 1

print(count)
