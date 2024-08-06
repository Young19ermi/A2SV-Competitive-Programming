def solve(n):
    possiblity = list(range(2,n+1))
    res = []
    used = [0]
    tot = sum(used)
    output = 0
    for i in range(len(possiblity)):

        used.append(possiblity[i])
        tot += possiblity[i]
        if tot == possiblity[i]:
            output += 1
            continue
        else:
            for n in used:
                if tot - n == possiblity[i]:
                    output += 1
                    continue
    return output
test = int(input())
for _ in range(test):
    n = int(input())
    print(solve(n))