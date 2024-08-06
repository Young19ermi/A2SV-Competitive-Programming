def solve(nums,test):
    odd = 0
    even = 0
    for n in nums:
        if n% 2==0:
            even+=1
        else:
            odd +=1 
    if odd==test and even ==test:
        return 'Yes'
    else:
        return 'No'

n = int(input())
for _ in range(n):
    test = int(input())
    nums = list(map(int,input().split()))

    print(solve(nums,test))