n, m = map(int, input().split())
grid= [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(m):
    col = int(input())
    col -= 1

    row = 0
    for r in range(n):
        bomb_size = grid[r][col]
        if bomb_size == 0:
            continue
        else:
            row = r
            break

    grid[row][col] = 0
    x, y = row, col
    for d in range(4):
        for step in range(1, bomb_size):
            nx = x + dx[d]*step
            ny = y + dy[d]*step

            if in_range(nx, ny):
                grid[nx][ny] = 0

    # 중력 적용
    for j in range(n):
        non_zero_elements = [grid[i][j] for i in range(n) if grid[i][j] != 0]
        for i in range(n):
            if i < n - len(non_zero_elements):
                grid[i][j] = 0
            else:
                grid[i][j] = non_zero_elements[i - (n - len(non_zero_elements))]


for row in grid:
    print(*row)