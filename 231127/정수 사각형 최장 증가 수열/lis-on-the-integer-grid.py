dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

ans = 0
def DFS(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1)

    return dp[x][y]

for i in range(n):
    for j in range(n):
        ans = max(ans, DFS(i, j))

print(ans)