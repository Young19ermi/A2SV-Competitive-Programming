testcase =int(input())
for _ in range(testcase):
    test =str(input())
    oper= list(map(int, test.split("+")))
    print(oper[0] + oper[1])