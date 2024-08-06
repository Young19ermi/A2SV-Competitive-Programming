import sys
 
 
def iinp():
    return int(sys.stdin.readline().strip())
 
 
def linp():
    return list(map(int, sys.stdin.readline().strip().split()))
 
 
def lsinp():
    return sys.stdin.readline().strip().split()
 
 
def digit():
    return [int(i) for i in (list(sys.stdin.readline().strip()))]
 
 
def char():
    return list(sys.stdin.readline().strip())
 
 
def string():
    return sys.stdin.readline().strip()
 
 
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil


 
def deletion(index):
    s = list(t)
    for i in range(index):
        j = permutation[i]
        s[j-1] = ''
    return ''.join(s)
 
def checker(a,b):
    stack = list(b)
    for val in reversed(a):
        if stack and stack[-1] == val:
            stack.pop()
    return not stack
 
t = input().strip()
p = input().strip()
permutation = list(map(int, input().split()))
left = -1
right = len(permutation)
 
 
 
 
while right > left +1:
    mid = (left + right ) // 2
 
    if checker(deletion(mid),p):
        left = mid
             
    else:
        right = mid  
       
    
print(left)