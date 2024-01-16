n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
bash_positions = [[x-1, y-1] for _ in range(m) for x, y in [map(int, input().split())]]


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


def move_bash(n, grid, bash_positions):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    new_grid = [[0] * n for _ in range(n)]

    for x, y in sorted(bash_positions):
        neighbor_values = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny, n):
                neighbor_values.append((grid[nx][ny], nx, ny))

        val, cur_x, cur_y = max(neighbor_values, key=lambda item: item[0])
        new_grid[cur_x][cur_y] += 1

    for x in range(n):
        for y in range(n):
            if new_grid[x][y] >= 2:
                new_grid[x][y] = 0

    updated_bash_positions = [(x, y) for x in range(n) for y in range(n) if new_grid[x][y] == 1]

    return updated_bash_positions



for _ in range(t):
    bash_positions = move_bash(n, grid, bash_positions)

print(len(bash_positions))