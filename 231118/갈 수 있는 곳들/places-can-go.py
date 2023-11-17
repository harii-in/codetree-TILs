from collections import deque
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

total = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 0

# 뱀이 없는 경우 1, 뱀이 있는 경우 0
def BFS(i, j):
    global total

    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if possible(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = True
                total += 1
    
    return

for _ in range(k):
    i, j = map(int, input().split())
    if possible(i, j):
        total += 1
        BFS(i, j)

print(total)