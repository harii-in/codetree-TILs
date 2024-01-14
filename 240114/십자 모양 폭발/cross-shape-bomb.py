n = int(input())
grid= [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())    # 1부터 시작인 점 유의

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
x=r-1
y=c-1
bomb_size = grid[x][y]

grid[x][y] = 0
for d in range(4):
    for step in range(1, bomb_size):
        nx = x + dx[d]*step
        ny = y + dy[d]*step

        if in_range(nx, ny):
            grid[nx][ny] = 0

# 중력 적용
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