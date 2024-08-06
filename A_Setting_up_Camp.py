def solve(a, b, c):
    
    total = 0
    total += a

    if b % 3 == 1:
        if c >= 2:
            b += 2
            c -= 2 
            
        else:
            return -1

    elif b % 3 == 2:
        if c >= 1:
            c -= 1
            b += 1
            
        else:
            return -1
    
    total += b//3
    total += c//3

    if c % 3 > 0:
        total += 1

    return total

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(solve(a,b,c))