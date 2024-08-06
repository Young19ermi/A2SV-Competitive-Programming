n = int(input())

s = 0
for _ in range(n):

    i = list(input())
    
    
    if "+" in i:
    
        s += 1
    elif "-" in i:
        s-=1 

print(s)
