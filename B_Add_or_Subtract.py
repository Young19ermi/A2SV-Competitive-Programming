testcase = int(input())
for _ in range(testcase):
    nums =list(map(int, input().split()))  
    if nums[0] + nums[1] == nums[2]:
        print("+")
    elif nums[0] - nums[1] == nums[2]:
        print("-")


