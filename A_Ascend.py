
def length(nums):
    n = len(nums)
    
    max_length = 1
    current_length = 1

    for i in range(1, n):
        
        if nums[i] > nums[i-1]:
            current_length += 1
        else:
            current_length = 1

        max_length = max(max_length, current_length)
        
    return max_length


n = int(input())
nums = list(map(int, input().split()))
print(length(nums))
