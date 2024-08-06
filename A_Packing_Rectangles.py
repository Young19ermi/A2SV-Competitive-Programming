from math import floor
w,h,n = map(int,input().split())


def solve(a,b,target):
    return floor(target / a) * floor(target / b) 


i = 0
j = max(w,h) * n
while j > i+1:
    mid = (i+ j) // 2
    
    if solve(w,h,mid) < n:
        i = mid
    else:
        j = mid

print(j)