inputs = input()
m,n = map(int, inputs.split())
tv = list(map(int, input().split()))

free = sorted(list(filter(lambda x: x<0, tv)))
if len(free) > n:
    res = 0
    for i in range(0,n):
        res += free[i]
    res = abs(res)
    print(res)
  
else:
    res = abs(sum(free))
    print(res)
  

        







