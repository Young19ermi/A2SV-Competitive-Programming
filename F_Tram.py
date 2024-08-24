def solve(enters,exits,n):
    
    l = 0
    maximum = []
    for i in range(n):
        l += int(enters[i]) - int(exits[i])
        maximum.append(l)
    return max(maximum)
n = int(input())
enters,exits = [],[]
for _ in range(n):
    x,y =input().split()
    enters.append(y)
    exits.append(x)
print(solve(enters,exits,n))