
def solve(n):
    count = 0
    

    while n != 0:
        if n >= k[0]:
            n -= 100
            
        elif n >= k[1]:
            n -= 20
            
        elif n >= k[2]:
            n -= 10
            
        elif n >= k[3]:
            n -= 5
        
        else:
            n -= 1
            
        count += 1
    return count
n = int(input())
k = [100,20,10,5,1]
print(solve(n))