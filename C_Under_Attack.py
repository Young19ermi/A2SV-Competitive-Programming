from collections import *
test = int(input())
for _ in range(test):
    leftdiagonal = defaultdict(int)
    rightdiagonal = defaultdict(int)
    rows = input(int)
    cols = input(int)
    matrix = []
    for _ in range(rows):
        temp = []
        for j in range(cols):
            temp.append(matrix[rows][cols])
    print(matrix)


    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            leftdiagonal[cols+rows] += matrix[rows][cols]
            rightdiagonal[rows-cols] += matrix[rows][cols]
    
    
        
                


        






