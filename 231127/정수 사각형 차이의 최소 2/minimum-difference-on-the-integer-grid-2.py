from collections import deque
# 상, 하, 좌, 우
dx = [1, 0]
dy = [0, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def DFS(x, y, min_val, max_val):
    global ans

    if x == n-1 and y == n-1:
        ans = min(ans, max_val - min_val)
        return

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]

        if in_range(nx, ny):
            next_min_val = min(min_val, grid[nx][ny])
            next_max_val = max(max_val, grid[nx][ny])
            DFS(nx, ny, next_min_val, next_max_val)

DFS(0, 0, grid[0][0], grid[0][0])
print(ans)