import math
 
 
for _ in range(int(input())):
    n = int(input())
    numo = math.floor(math.log(n,2))
    print(2**numo)