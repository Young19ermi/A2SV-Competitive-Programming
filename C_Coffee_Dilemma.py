def solve(nums):
    def dp(index,state):
        res = 0
        if index == len(nums):
            return 0
        if state:
            take = solve(index+1, )
        take = dp(index)



test = int(input())
nums = list(map(int, input().split()))
print(solve(nums))