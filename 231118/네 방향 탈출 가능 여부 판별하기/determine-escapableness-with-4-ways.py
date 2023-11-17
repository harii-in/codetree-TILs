from collections import deque
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def possible(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1

# 뱀이 없는 경우 1, 뱀이 있는 경우 0
def BFS():
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1 and not visited[x][y]:
            return 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if possible(nx, ny):
                queue.append((nx, ny))
    
    return 0

print(BFS())