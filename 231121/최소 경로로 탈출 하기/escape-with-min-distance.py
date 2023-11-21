from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def possible(x, y):
    return in_range(x, y) and visited[x][y] == 0 and grid[x][y] == 1

def BFS():
    global visited

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y]


        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if possible(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return -1

print(BFS())