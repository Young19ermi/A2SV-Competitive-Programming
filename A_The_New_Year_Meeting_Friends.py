res = list(map(int, input().split()))
res.sort()

r = 0
r += max(res) - res[1]
r += res[1] - min(res)
print(r)

