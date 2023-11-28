n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = grid[0][0]

# 첫 번째 행의 dp 값
# 이전 열의 dp 값과 현재 위치의 grid 값을 비교하여 더 큰 값을 저장
for j in range(1, n):
    dp[0][j] = max(dp[0][j-1], grid[0][j])

# 첫 번째 열의 dp 값
# 이전 행의 dp 값과 현재 위치의 grid 값을 비교하여 더 큰 값을 저장
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], grid[i][0])

# 나머지 dp 값
# 이전 행의 dp 값, 이전 열의 dp 값, 현재 위치의 grid 값을 비교하여 가장 큰 값을 저장
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[n-1][n-1])