n,k,x = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse= True)

sum  = 0
for i in range(0,k):
    sum += x

for i in range(k, len(nums)):
    sum += nums[i]

print(sum)