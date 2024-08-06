# x_axis = int(input())

# steps = [1,2,3,4,5]
# count = 0
# sum = 0
# for i in range(len(steps)-1,-1,-1):
#     if sum < x_axis:
#         sum += steps[i]
#         count += 1
#     else:
#         print(count)
#         break
from math import ceil
x = int(input())

n = [1,2,3,4,5]
n.sort(reverse = True)
res = 0
print(ceil(x/5))


f