
def solve(nums):
    for i in range(len(nums)-2):
        if nums[i] < 0:
            return 'NO'
        
        curr = nums[i]
        nums[i] -= curr
        nums[i+1] -= 2*curr
        nums[i+2] -= curr

    if nums != [0] * len(nums):
        return 'NO'
    else:
        return 'YES'

test = int(input())
for _ in range(test):
    length = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))