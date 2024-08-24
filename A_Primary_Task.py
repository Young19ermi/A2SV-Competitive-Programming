def solve(num):
    k = list(str(num))
    k = k[::-1]
    index = 0
    for i in range(len(k)):
        if int(k[i]) > 0 and k[i+1] == 0:
            index = i
            break
    for i in range(index,len(k)):
        s



n =int(input())
for _ in range(n):
    num = int(input())
    print(solve(num))