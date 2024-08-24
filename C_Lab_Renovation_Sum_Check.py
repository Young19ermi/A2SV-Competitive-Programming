n = int(input())
grid = []
for _ in range(n):
  row = list(map(int, input().split()))
  grid.append(row)

good = True
for i in range(n):
  for j in range(n):
    if grid[i][j] != 1:
      found = False
      for s in range(n):
        for t in range(n):
          if grid[i][j] == grid[i][s] + grid[t][j]:
            found = True
            break
        if found:
          break
      if not found:
        good = False
        break
  if not good:
    break

if good:
  print("Yes")
else:
  print("No")