# testcase = int(input())
# for _ in range(testcase):
#     inputs =input()
#     length, maxswap = map(int, inputs.split())
#     array = list(map(int, input().split()))
#     def flip(array, k): 
#             i, j = 0, k
#             while i < j:
#                 array[i], array[j] = array[j], array[i]
#                 i += 1
#                 j -= 1
#     flips = []
#     n = len(array)
#     count = 0
#     for i in range(n-1, 0 ,-1):
#         max_index = array.index(max(array[:i+1]))
#         if max_index != i:
#             flip(array, max_index)                    
#             flip(array, i)
#             count += 1
#     if count > maxswap:
#          print("NO")
#     else:
#          print("YES")
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if sorted(arr) == arr or k > 1:
        print("YES")
    else:
        print("NO")

    
            
            


