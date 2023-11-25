n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = grid[0][0]

# 첫 번째 행의 dp 값
# 이전 열의 dp 값과 현재 위치의 grid 값을 비교하여 더 작은 값을 저장
for j in range(1, n):
    dp[0][j] = min(dp[0][j-1], grid[0][j])

# 첫 번째 열의 dp 값
# 이전 행의 dp 값과 현재 위치의 grid 값을 비교하여 더 작은 값을 저장
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], grid[i][0])

# 나머지 dp 값
# 이전 행의 dp 값, 이전 열의 dp 값, 현재 위치의 grid 값을 비교하여 가장 작은 값을 저장
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])


# 시간초과
# dx = [1, 0]
# dy = [0, 1]

# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# ans = []
# def DFS(x, y, tmp):
#     if x == n-1 and y == n-1:
#         ans.append(tmp)
#         return

#     for d in range(2):
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if in_range(nx, ny) and not visited[nx][ny]:
#             visited[nx][ny] = True
#             DFS(nx, ny, min(tmp, grid[nx][ny]))
#             visited[nx][ny] = False

# DFS(0, 0, grid[0][0])
# print(max(ans))