from math import *
n = int(input())
def solve(n):
    if n == 0 or n == 1 or n==2:
        return 0
    
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2,int(sqrt(n))+1):
        if primes[i] == True:
            for i in range(i*i,n+1,i):
                primes[i] = False
    ans = []
    
    for i in range(0,len(primes)-1):
        if primes[i] == True:
            ans.append(i)
    
    numbers = []

    for x in range(2,n+1):
        if x not in ans:
            numbers.append(x)
    count = 0
    res = 0
    for n in numbers:
        count = 0
        for j in ans:
            if n % j == 0:
                count += 1
        if count == 2:
            # print(i,j)
            res += 1

    return res
print(solve(n))

# res = list(map(lambda x:sorted(x), res))
# res = list(sorted(res, key = lambda x:x[0]))








