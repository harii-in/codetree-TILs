dx = [1, 0]
dy = [0, -1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[1e9]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def DFS(x, y):
    if x == n-1 and y == 0:
        return grid[x][y]

    if dp[x][y] != 1e9:
        return dp[x][y]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if in_range(nx, ny):
            dp[x][y] = min(dp[x][y], grid[x][y] + DFS(nx, ny))

    return dp[x][y]

print(DFS(0, n-1))