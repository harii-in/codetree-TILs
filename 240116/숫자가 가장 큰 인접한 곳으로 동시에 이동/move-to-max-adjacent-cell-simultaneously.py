def input_data():
    """데이터 입력: 격자와 초기 bash 위치"""
    n, m, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    bash_positions = [[x-1, y-1] for _ in range(m) for x, y in [map(int, input().split())]]
    return n, m, t, grid, bash_positions


def in_range(x, y, n):
    """(x, y)가 n x n 크기의 격자 내부에 있는지 확인"""
    return 0 <= x < n and 0 <= y < n


def move_bash(n, grid, bash_positions):
    """각 bash를 주변의 최대값 위치로 이동"""
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


n, m, t, grid, bash_positions = input_data()

for _ in range(t):
    bash_positions = move_bash(n, grid, bash_positions)

print(len(bash_positions))