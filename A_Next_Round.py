from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

n = input().split()
nums = list(map(int, input().split()))

res = 0
l = nums[int(n[1])-1]
for k in nums:
    if k >= l and k > 0:
        res += 1
print(res)