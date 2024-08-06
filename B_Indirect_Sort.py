def solve(nums):
    
    res = []
    if nums == sorted(nums):
        return 'YES'

    
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(i+2,len(nums)):
                if nums[i] > nums[k] and nums[i] != nums[j]:
                    nums[i] = nums[i] + nums[j]
                    res.append(nums[i] + nums[j])
                else:
                    nums[j],nums[k] = nums[k],nums[j]
                    res.append(nums[k])
                    res.append(nums[j])
             
    print(res)   
    if nums == sorted(nums):
        return 'YES'
    else:
        return 'NO'



testcase= int(input())

for _ in range(testcase):
    length = int(input())

    nums = list(map(int, input().split()))
    print(solve(nums))

for i in range(len(numd)):
    for j in ragne(len(nums)):
        init = nums[0]

        if init == nums[0]:
            return init
        refix_Sum = [0] * len(nums)
