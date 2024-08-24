def solve(n):
    n = n+1
    while True:
        l = list(str(n))
        if len(set(l)) == len(l):
            return n
        else:
            n += 1

n = int(input(" "))
print(solve(n))
