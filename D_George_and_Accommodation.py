def solve(nums):
    count = 0
    for x,y in nums:
        if int(y)-int(x) >= 2:
            count += 1
    return count

n = int(input())
nums = []
for _ in range(n):
    x,y = input().split()
    nums.append([x,y])
print(solve(nums))


