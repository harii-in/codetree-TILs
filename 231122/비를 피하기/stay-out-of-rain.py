from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, h, m = map(int, input().split())
# 숫자 0은 해당 칸이 이동할 수 있는 곳
# 숫자 1은 벽이 있어 해당 칸이 이동할 수 없는 곳
# 숫자 2는 해당 칸에 사람이 서있음
# 숫자 3는 해당 공간이 비를 피할 수 있는 공간
grid = [list(map(int, input().split())) for _ in range(n)]
# 해당 위치에 있는 사람이 절대 비를 피할 수 없다면 -1을 출력
visited = [[-1]*n for _ in range(n)]

# 각 사람 위치마다 공간 찾기 vs 각 공간마다 사람 찾기
# 공간에서 시작하여 BFS를 수행하면, 모든 공간을 한 번만 방문하므로 시간 복잡도를 줄일 수 있음
# 사람의 위치마다 BFS를 수행하면, 같은 공간을 여러 번 방문해야 하므로 시간 복잡도가 증가
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y):
    return in_range(x, y) and grid[x][y] != 1 and visited[x][y] == -1

def BFS():
    global visited
    queue = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
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

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:  # 사람이 있는 위치
            print(visited[i][j] if visited[i][j] != -1 else -1, end=' ')
        else:
            print(0, end=' ')
    print()