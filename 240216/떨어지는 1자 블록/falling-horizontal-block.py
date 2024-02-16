n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
flag = False

for row in range(n):
    for col in range(k - 1, k - 1 + m):
        # 블럭이 존재하면
        if grid[row][col] == 1:
            # 바로 위에 블럭 두기
            for j in range(k - 1, k - 1 + m):
                grid[row - 1][j] = 1
            flag = True
            break
    if flag:
        break
        
if not flag:
        for col in range(k - 1, k - 1 + m):
            grid[n-1][col] = 1

for row in grid:
    print(*row)