testcase = int(input())
for _ in range(testcase):
    words = input()
    if len(set(words)) == 1:
        print( -1)
    else:
        print(len(words)-1)