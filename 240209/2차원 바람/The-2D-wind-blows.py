N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
wind = [list(map(int, input().split())) for _ in range(Q)]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < M

def rotate(r1, c1, r2, c2):
    up = grid[r1][c1:c2]
    right = [grid[r][c2] for r in range(r1, r2)]
    down = grid[r2][c1+1:c2+1]
    left = [grid[r][c1] for r in range(r1+1, r2+1)]

    up.insert(0, left[0])
    right.insert(0, up[-1])
    down.append(right[-1])
    left.append(down[0])

    up.pop(-1)
    right.pop(-1)
    down.pop(0)
    left.pop(0)

    grid[r1][c1:c2] = up
    grid[r2][c1+1:c2+1] = down

    for i in range(r1, r2):
        grid[i][c2] = right[i - r1]

    for i in range(r1+1, r2+1):
        grid[i][c1] = left[i - (r1+1)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def average(r1, c1, r2, c2):
    new_grid = [row[:] for row in grid]
    for x in range(r1, r2+1):
        for y in range(c1, c2+1):
            tmp_sum = grid[x][y]
            cnt = 1

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if inRange(nx, ny):
                    tmp_sum += grid[nx][ny]
                    cnt += 1

            new_grid[x][y] = tmp_sum // cnt
    return new_grid


for w in wind:
    r1, c1, r2, c2 = w
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    rotate(r1, c1, r2, c2)
    # for row in grid:
    #     print(*row)
    grid = average(r1, c1, r2, c2)

# print()
for row in grid:
    print(*row)