def solve(num, k):
  count = 0
  while num > 0:
    digit = num % 10
    if digit == 4 or digit == 7:
      count += 1
    num //= 10
  return count <= k

n, k = map(int, input().split())
nums = list(map(int, input().split()))

lucky_count = 0
for num in nums:
  if solve(num, k):
    lucky_count += 1

print(lucky_count)