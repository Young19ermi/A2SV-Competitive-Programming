num = int(input())
nums = str(num)
l = []
for n in nums:
    l.append(int(n))
m = max(l)
change = 9 - m
for n in l:
    if n == m:
        m = change
print(l)