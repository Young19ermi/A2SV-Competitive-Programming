test = int(input())
for _ in range(test):
    n,m = input().split()
    n = list(n)
    m = list(m)

    k = n[0]
    l = m[0]

    n.remove(k)
    m.remove(l)
    print(l+"".join(n), k+"".join(m))