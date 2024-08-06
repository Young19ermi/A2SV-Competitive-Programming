test = int(input())
number = pow(5, test) % 100
n = str(number)

k = list(n.strip())
k = list(reversed(k))
res = []
for n in range(2):
    res.append(k[n])
r = list(reversed(res))
print("".join(r))

