n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
flag = False
r = 0

for row in range(n-1, -1, -1):
    for col in range(k - 1, k - 1 + m):
        if grid[row][col] == 1:
            flag = False
            break
        elif grid[row][col] == 0:
            flag = True
    if flag:
        r = row
        break

if flag:
    for col in range(k - 1, k - 1 + m):
        grid[r][col] = 1

for row in grid:
    print(*row)