def solve(nums):
    lucky = 0
    for n in nums:
        if n != '4' and n != '7':
            break
    else:
        return 'YES'
    for n in nums:
        if n == '4' or n=='7':
            lucky += 1
    if lucky == 7 or lucky == 4:
        return 'YES'
    else:
        return 'NO'
n = int(input())
nums = list(str(n))
print(solve(nums))