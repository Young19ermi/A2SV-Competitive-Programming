# test = int(input())
# for _ in range(test):
#     matrow = list(map(int, input().split()))
#     testcase =len(matrow)
#     for row in range(testcase):
#         sum += matrow[row][row] 
#         sum += matrow[row][testcase-1-row]
#     for row in range(testcase):
#         for col in range(testcase):
#             if row == testcase//2:
#                 sum += matrow[row][col]
#             if col == testcase//2:
#                 sum += matrow[row][col]
#     sum -= 3* matrow[testcase//2][testcase//2]
#     print(sum)
testcase = int(input())

mat = []
for _ in range(testcase):
    row = list(map(int, input().split()))
    mat.append(row)
sum = 0
for i in range(testcase):
    sum += mat[i][i]  
    sum += mat[i][testcase-1-i]  
    sum += mat[testcase//2][i]  
    sum += mat[i][testcase//2]  
sum -= 3 * mat[testcase//2][testcase//2]
print(sum)
