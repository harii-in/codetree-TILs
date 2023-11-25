dx = [1, 0]
dy = [0, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

ans = []
def DFS(x, y, tmp):
    if x == n-1 and y == n-1:
        ans.append(tmp)
        return

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if in_range(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            DFS(nx, ny, min(tmp, grid[nx][ny]))
            visited[nx][ny] = False

DFS(0, 0, grid[0][0])
print(max(ans))