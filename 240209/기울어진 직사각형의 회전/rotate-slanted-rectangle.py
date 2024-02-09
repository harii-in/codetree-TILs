import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
new_grid = copy.deepcopy(grid)

r, c, m1, m2, m3, m4, direction = map(int, input().split())
dists = [m1, m2, m3, m4]
x = r - 1
y = c - 1

# 0 반시계, 1 시계
dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]
if direction == 0:
    for d in range(4):
        for dist in range(dists[d]):
            nx = x + dx[d]
            ny = y + dy[d]
            new_grid[nx][ny] = grid[x][y]
            x, y = nx, ny
elif direction == 1:
    for d in range(3, -1, -1):
        for dist in range(dists[3 - d]):
            nx = x + dx[d]
            ny = y + dy[d]
            new_grid[nx][ny] = grid[x][y]
            x, y = nx, ny


for row in new_grid:
    print(*row)