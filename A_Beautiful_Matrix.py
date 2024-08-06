
matrix = [list(map(int, input().split())) for _ in range(5)]

row = 0
col = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i
            col = j

moves = abs(2 - row) + abs(2 - col)
print(moves)
