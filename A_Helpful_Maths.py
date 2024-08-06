

n = list(map(int,input().split('+')))
n.sort()
res = ""
for i in range(len(n)):
    res += str(n[i])
    res += str('+')
k = list(res)
k.pop()
print("".join(k))