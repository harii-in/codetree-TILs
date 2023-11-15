# 아래, 오른쪽
dx = [1, 0]
dy = [0, 1]

n, m = map(int, input().split())

# 뱀이 없는 경우 1, 뱀이 있는 경우 0
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력
flag = False
def DFS(x, y):
    global flag
    if x == n-1 and y == m-1 and grid[x][y] == 1:
        flag = True
        print(1)
        return
    
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx, ny)

visited[0][0] = True
DFS(0, 0)
if not flag:
    print(0)