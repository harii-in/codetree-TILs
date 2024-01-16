n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
positions = [[x-1, y-1] for _ in range(m) for x, y in [map(int, input().split())]]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def move_bash(positions):
    new_grid = [[0] * n for _ in range(n)]

    # 상하좌우로 인접한 곳에 있는 숫자들 중 가장 큰 값으로 이동
    for x, y in sorted(positions):
        neighbor = []
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if in_range(nx, ny):
                neighbor.append((grid[nx][ny], nx, ny))

        val, cur_x, cur_y = max(neighbor, key=lambda item: item[0])
        new_grid[cur_x][cur_y] += 1

    #  2개 이상의 구슬 위치가 동일하다면, 해당 위치에 있는 구슬들은 전부 사라짐
    for x in range(n):
        for y in range(n):
            if new_grid[x][y] >= 2:
                new_grid[x][y] = 0

    updated_positions = [(x, y) for x in range(n) for y in range(n) if new_grid[x][y] == 1]

    return updated_positions


for _ in range(t):
    positions = move_bash(positions)

print(len(positions))