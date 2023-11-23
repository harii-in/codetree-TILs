from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())

grid = []
bad_mandarin = []
visited = [[-2]*n for _ in range(n)]
# 0은 해당 칸에 아무것도 놓여있지 않음
# 숫자 1은 해당 칸에 귤이 놓여있음
# 숫자 2는 해당 칸에 상한 귤이 처음부터 놓여 있음
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(n):
        if row[j] == 0:
            visited[i][j] = -1
        elif row[j] == 2:
            bad_mandarin.append((i, j))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y):
    return in_range(x, y) and grid[x][y] == 1 and visited[x][y] == -2

# 처음부터 비어있던 칸이라면 -1을 출력
# 끝까지 상하지 않는 귤이라면 -2를 출력
def BFS():
    global visited

    queue = deque()
    for i, j in bad_mandarin:
        queue.append((i, j))
        visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if possible(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

BFS()
for row in range(n):
    print(*visited[row])