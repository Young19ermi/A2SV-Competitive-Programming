
def solve(num, k):
    while k > 0:
        if num % 10 > 0:
            num -= 1
        else:
            num //= 10
        k -= 1
    return num

# Reading input and calling the solve function
nums = list(map(int, input().split()))
num = nums[0]
k = nums[1]

print(solve(num, k))
