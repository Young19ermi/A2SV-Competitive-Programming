testcase = int(input())

length = input()
nums = list(map(int, input().split()))
count = 0
i = 0
j = 0
sign = False
negative = True
while i <= len(nums)-1 and j <= len(nums)-1:
    if nums[j] < 0:
        i = j