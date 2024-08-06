test = int(input())
for _ in range(test):
    n,x = map(int, input().split())

    nums = list(map(int, input().split()))
    nums.sort()
    left = []
    right = []
    for i in range(len(nums)//2):
        left.append(nums[i])
    for i in range(len(nums)//2, len(nums)):
        right.append(nums[i])

    for i in range(len(left)):
        if right[i] - left[i] < x:
            print('NO')
            break
    else:
        print('YES')    