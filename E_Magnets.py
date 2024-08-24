def solve(var):
    count = 1
    for i in range(len(var)-1):
        if var[i][0] == var[i+1][1]:
            count += 1
    return count


n = int(input())
var = []
for _ in range(n):
    k = input()
    var.append(list(k))
print(solve(var))