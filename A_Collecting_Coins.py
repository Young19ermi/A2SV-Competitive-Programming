def solve(nums,n):
  
    nums.sort()
    n -= 2 * nums[2] - nums[1] - nums[0]
    if n < 0 or n % 3 != 0:
        return "NO"
    else:
        return "YES"

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    n = nums[-1]
    nums.pop()

    print(solve(nums,n))


aabaaab