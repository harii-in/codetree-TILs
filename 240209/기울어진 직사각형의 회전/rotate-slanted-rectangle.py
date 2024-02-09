import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
new_grid = copy.deepcopy(grid)

r, c, m1, m2, m3, m4, direction = map(int, input().split())
dists = [m1, m2, m3, m4]
x = r - 1
y = c - 1

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

# 0 반시계, 1 시계
dx_cc = [-1, -1, 1, 1]
dy_cc = [1, -1, -1, 1]

dx_c = [1, 1, -1, -1]
dy_c = [-1, 1, 1, -1]

if direction == 0:
    for d in range(4):
        for dist in range(dists[d]):
            nx = x + dx_cc[d]
            ny = y + dy_cc[d]
            if inRange(nx, ny):
                new_grid[nx][ny] = grid[x][y]
                x, y = nx, ny
elif direction == 1:
    for d in range(4):
        for dist in range(dists[d]):
            nx = x + dx_c[d]
            ny = y + dy_c[d]
            if inRange(nx, ny):
                new_grid[nx][ny] = grid[x][y]
                x, y = nx, ny

for row in new_grid:
    print(*row)