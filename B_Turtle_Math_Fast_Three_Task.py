def solution(nums):
    if sum(nums) % 3 == 0:
        return 0
    res= 0
    total = sum(nums)
    for n in nums:
        if (total - n) % 3 == 0:
            return 1
            break
        
    
    return 3 - (total%3)
    
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(nums))












    # for n in nums:
    #     if (total - n) % 3 == 0:
    #         return 1
    #         break

    # for n in nums:
    #     if (total + n) % 3 == 0:
    #         minimum.append(n)
    #     if (total + 1) % 3==0:
    #         minimum.append(1)
    #     if total == 10:
    #         return 2
        
    # if minimum:
    #     return min(minimum)
    # else:
    #     res = 0
    #     while n % 3 == 0:
    #         n += 1
    #         res += 1
    #     minimum.append(res)
    #     return min(minimum)