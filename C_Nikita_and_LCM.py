from functools import reduce

def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def lcm(a, b):
    return (a * b) // gcf(a, b)

def refine(nums):
    return reduce(lcm, nums)

def solve(nums):
    nums.sort()
    if len(nums) == 1:
        return 0
    stack = [nums[0]]
    initial = stack
    k = refine(stack)
    for i in range(1,len(nums)):
        stack.append(nums[i])
        b = lcm(k,nums[i])
        if lcm(k,nums[i]) in stack:
            stack.remove(b)
        k = b
    if len(stack) == 1 and stack == initial:
        stack.pop()
    return len(stack)
    
test = int(input())
for _ in range(test):
    length = int(input())
    nums = list(map(int, input().split()))
    print(solve(nums))


