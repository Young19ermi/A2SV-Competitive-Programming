
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
s = 0
for i in range(n // 2):
    k = nums[i] + nums[n - 1 - i]
    s += k ** 2
print(s)


