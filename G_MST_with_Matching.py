def solve(i,e,u):

    count = 0
    count_e = 0

    count += i
    if e % 3 == 0:
        count_e += e//3
    else:
        return -1
    if u % 3 == 0:
        count += u//3
    else:
        count += u//3 + u %3
    return count + count_e
    

testcase = input()
for _ in range(int(testcase)):
    i,e,u = map(int, input().split())
    print(solve(i,e,u))