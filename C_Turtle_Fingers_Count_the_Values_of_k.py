import math
testcase = int(input())
for _ in range(testcase):
    a,b,l = input().split()
    i = 0
    count_a = []
    count_b = []
    
    while math.pow(int(a),int(i)) <= int(l):
        if int(l) % math.pow(int(a),int(i)) == 0:
            count_a.append(math.pow(int(a),int(i)))
        i+=1

    i = 0
    while pow(int(b),int(i)) <= int(l):
        if int(l) % pow(int(b),int(i)) == 0:
            count_b.append(pow(int(b),int(i)))
        i += 1

    oper = set()

    for i in range(len(count_a)):
        for j in range(len(count_b)):
            oper.add(count_a[i] * count_b[j])
    print(len(oper))
    