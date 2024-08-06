testcase =int(input())
for i in range(testcase):
    length, queries = map(int, input().split())
    e= list(map(int, input().split()))
    query = list(map(int, input().split()))
    #elem =sorted(e)
    res = []
    for i in range(len(e)):
        for j in range(len(query)-1):
            if (e[i] / 2*query[j]) % 1 == 0:
                e[i] += 2*query[j-1]
                res.append(e[i])
                break
            else:
                res.append(e[i])
                break
    print(res)

