from math import *
from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    if b % a == 0:
        return b * (b//a)
    else:
        return b *(a//math.gcd(a,b))


 
 
 
 
t = I()
for _ in range(t):
    a,b = II()
    solve()
