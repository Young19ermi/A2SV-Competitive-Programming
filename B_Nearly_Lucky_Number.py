n = int(input())
nums = list(str(n))
t=nums.count('4')
l =nums.count('7')
tot = t+l
if tot == 4 or tot == 7:
    print('YES')
else:
    print('NO')
