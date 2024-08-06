from collections import Counter
testcases = int(input())
for _ in range(testcases):
    length = int(input())
    nums = list(map(int, input().split()))
    flag = True
    to = nums[0]
    right = 0
    left = 0
    for i in range(len(nums)):
        if nums[i] == to and flag:
            left = i
            right = i
        else:
            right = i
            flag = False
        if not flag and nums[i] != to:
            right = i
    
    res1 = right - left

    
    nums = nums[::-1]
    right = 0
    flag = True
    left = 0
    to = nums[0]
    for i in range(len(nums)):
        if nums[i] == to and flag:
            left = i
            right = i
        else:
            flag = False
        
        if not flag and nums[i] != to:
            right = i
    res2 = right - left
    print(min(res1,res2))


         
         

