from math import *
test = int(input())
nums = list(map(int, input().split()))
ans  = gcd(nums[0])

for i in range(1,len(nums)):
    ans = gcd(ans,nums[i])

new = [] 

for i in range(len(nums)):
    new.append(nums[i] // ans)


k  = gcd(nums[0])

for i in range(1,len(new)):
    k = gcd(k,new[i])

res = [] 

for i in range(len(nums)):
    res.append(nums[i] // ans)
if len(set(res)) < len(nums):
    print('Yes')
else:
    print('No')
    