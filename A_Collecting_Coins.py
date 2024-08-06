def solve(num):
    n = nums.pop()
    n -= 2 * nums[2]- nums[1]- nums[0]
    if n < 0 or n % 3 != 0:
        return 'NO'
    else:
        return "YES"

test = int(input())
for _ in range(test):
    nums = list(map(int, input().split()))
    print(solve(nums))