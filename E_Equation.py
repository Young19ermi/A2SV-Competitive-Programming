from math import sqrt

k = float(input())


left = 0
right = k

p = 1e-6

while right > p + left:
    
    mid = ((left + right) / 2) 

    if mid** 2 + sqrt(mid)  > k:
        right = mid 
    else:
        left = mid

print(left)



