from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
grid = []
walls = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(n):
        if row[j] == 1:
            walls.append((i, j))

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

def BFS(remove_walls):
    for x, y in remove_walls:
        grid[x][y] = 0

    queue = deque()
    queue.append((r1, c1))
    visited = [[-1]*n for _ in range(n)]
    visited[r1][c1] = 0

    while queue:
        x, y = queue.popleft()

        if x == r2 and y == c2:
            return visited[x][y]

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and grid[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    for x, y in remove_walls:
        grid[x][y] = 1

    return 1e9

ans = 1e9
for remove_walls in combinations(walls, k):
    ans = min(ans, BFS(remove_walls))

print(ans if ans != 1e9 else -1)