from math import floor,ceil
def solve(nums,h):
    tot = 0
    for n in nums:
        if n < h:
            tot+=1
        else:
            tot += ceil(n/h)
    return tot

n,h = input().split()
nums= list(map(int,input().split()))
print(solve(nums,int(h)))