matrix = []
testcase =int(input()) 
for i in range(testcase):
    elem = list(map(int, input().split()))
    matrix.append(elem)
cols = len(matrix[0])
rows = len(matrix)
count = 0
res= 0 
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
           count += 1
    if count > 1:
        res += 1
    count = 0
  

print(res)

"""

for i in range(rows):
    for j in range(cols):
        if elem[rows][cols] == 1:
            count += 1
            rows+=1
            cols+=1
        else:
            continue
        print(count)

"""
