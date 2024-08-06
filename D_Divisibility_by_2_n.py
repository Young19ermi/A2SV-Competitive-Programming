
# gcd function

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
# primes
def prime_factorization(n):
    factors = []
    
    for divisor in range(2, n + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
    
    return factors

    #sieve n segmented
    def sieve(self, lim):
        primes = []
        is_p = [True] * (lim + 1)
        is_p[0] = is_p[1] = False
        for i in range(2, int(math.sqrt(lim)) + 1):
            if is_p[i]:
                primes.append(i)
                for j in range(i * i, lim + 1, i):
                    is_p[j] = False
        return primes

    def closestPrimes(self, l: int, r: int) -> list[int]:
        lim = int(math.sqrt(r)) + 1
        primes = self.sieve(lim)
        
        is_p = [True] * (r - l + 1)
        for p in primes:
            start = max(p * p, (l + p - 1) // p * p)
            for j in range(start, r + 1, p):
                is_p[j - l] = False
                
        if l == 1:
            is_p[0] = False
        
        res = [i + l for i in range(r - l + 1) if is_p[i]]
        
        return res
# (a + b) % m = (a%m + b%m) % m
# ● (a - b) % m = (a%m - b%m) % m
# ● (a*b)%m = (a%m * b%m) % m
# ● If (a - b) % m = 0, then a%m = b%m

#gcd(a,b)=xp⋅q,x=b⋅p= b ⋅ (a//gcd(a,b))


#b % a == 0
#x = b * (b//a)
#b % a != 0
#x = b *(a//gcd(a,b))e










