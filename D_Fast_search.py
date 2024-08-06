
# from bisect import bisect_left, bisect_right

# n = int(input())
# array = sorted(list(map(int, input().split())))
# k = int(input())

# for _ in range(k):
#     l, r = map(int, input().split())
    
#     left_index = bisect_left(array, l)
#     right_index = bisect_right(array, r)
#     count = right_index - left_index
#     print(count, end=' ')

def count_elements_less_than_or_equal(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return left


n = int(input())
arr = list(map(int, input().split()))
k = int(input())


arr.sort()
prefix_sum = [0] * n
prefix_sum[0] = 1 if arr[0] <= arr[0] else 0
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + (1 if arr[i] <= arr[i] else 0)


for _ in range(k):
    l, r = map(int, input().split())
    count_l = count_elements_less_than_or_equal(arr, l - 1)
    count_r = count_elements_less_than_or_equal(arr, r)
    
    result = count_r - count_l
    print(result, end=" ")
