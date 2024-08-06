
# testcase = int(input())
# for _ in range(testcase):
#     length = int(input())
#     test = list(map(int, input().split())) 
     

#     i = 0
#     j = i+1
#     while i < len(test) and j < len(test):
#         if abs(test[i] - test[j]) > 1:
#             print('NO')
#             break
#         i += 1
#         j += 1
#     print('YES')
testcase = int(input())

for _ in range(testcase):
    length = int(input())
    test = list(map(int, input().split())) 
    test.sort()
    i = 0
    j = i + 1
    can = True
    while i < len(test) and j < len(test):
        if abs(test[i] - test[j]) > 1:
            can = False
            print('NO')
            break
        i += 1
        j += 1
    
    if can:
        print('YES')
