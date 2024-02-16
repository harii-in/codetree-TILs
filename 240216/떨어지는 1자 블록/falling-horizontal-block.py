n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
flag = False
for row in range(n):
    for col in range(k - 1, k - 1 + m):
        if grid[row][col] == 1:
            for j in range(k - 1, k - 1 + m):
                grid[row - 1][j] = 1
            flag = True
            break
    if flag:
        break
        
if not flag:
    for row in range(n):
        for col in range(k-1,k-1+m):
            grid[row][col] = 1

for row in range(n):
    for col in range(n):
        print(grid[row][col], end=' ')
    print()