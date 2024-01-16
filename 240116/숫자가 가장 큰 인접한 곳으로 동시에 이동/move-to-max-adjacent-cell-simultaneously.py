n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

positions = [[x-1, y-1] for _ in range(m) for x, y in [map(int, input().split())]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(positions):
    new_grid = [[0] * n for _ in range(n)]

    for x, y in sorted(positions):
        neighbor = []
        # 상하좌우 중 가장 큰 값이 적혀있는 숫자
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if in_range(nx, ny):
                neighbor.append((grid[nx][ny], nx, ny))

        value, next_x, next_y = max(neighbor, key=lambda item: item[0])
        new_grid[next_x][next_y] += 1

    # 이동한 이후 2개 이상의 구슬 위치가 동일하면, 해당 위치에 있는 구슬들은 전부 사라짐
    for x in range(n):
        for y in range(n):
            if new_grid[x][y] >= 2:
                new_grid[x][y] = 0

    updated_position = [(x, y) for x in range(n) for y in range(n) if new_grid[x][y] == 1]

    return updated_position


for _ in range(t):
    positions = move(positions)

print(len(positions))