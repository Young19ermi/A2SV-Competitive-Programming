def solve(nums, c,d,n):
    k = d-c
    p = d+c
    nums = sorted(nums)
    count = 0
    for i in range(1,len(nums)-1):
     
        q = set()
        if nums[i] + p not in nums and nums[i] - k not in nums:
            return "NO"
        q.add(nums[i])
        
    else:
        return "YES"

test = int(input())
for _ in range(test):
    n,c,d = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve(nums,c,d,n))

     