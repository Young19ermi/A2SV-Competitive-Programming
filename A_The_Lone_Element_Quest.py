testcases = int(input())
for _ in range(testcases):
    length = int(input())
    nums = list(map(int, input().split()))
    count = {num:nums.count(num) for num in nums}
    for items,value in count.items():
        if value == 1:
            res = items
    print(nums.index(res)+1)
