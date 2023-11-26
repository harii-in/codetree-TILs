# 상, 하, 좌, 우
dx = [1, 0]
dy = [0, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 경로에 포함된 값들의 최대값이 최소가 되는 경로의 최대값을 반환
def check():
    dp = [[1e9]*n for _ in range(n)]
    # 시작점의 값을 DP 테이블에 저장
    dp[0][0] = grid[0][0]

    # 첫 번째 행의 모든 칸 - 현재 열까지의 최댓값
    for j in range(1, n):
        dp[0][j] = max(dp[0][j-1], grid[0][j])
    
    # 첫 번째 열의 모든 칸 - 현재 열의 행까지의 최댓
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], grid[i][0])

    # 위쪽 칸과 왼쪽 칸 중에서 최소가 최대인?
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])
    
    return dp[n-1][n-1]  # 1e9면 경로 없음!

ans = 1e9
# 그리드의 모든 칸을 순회하면서, 각 칸의 값이 low보다 작으면 그 칸의 값을 무한대(1e9)로 설정
for low in range(1, 101):
    for i in range(n):
        for j in range(n):
            if grid[i][j] < low:
                grid[i][j] = 1e9

    tmp = check()
    if tmp < 1e9:
        ans = min(ans, abs(tmp-low))

print(ans)

# # time out
# ans = 1e9

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# def DFS(x, y, min_val, max_val):
#     global ans

#     if x == n-1 and y == n-1:
#         ans = min(ans, max_val - min_val)
#         return

#     for i in range(2):
#         nx, ny = x + dx[i], y + dy[i]

#         if in_range(nx, ny):
#             next_min_val = min(min_val, grid[nx][ny])
#             next_max_val = max(max_val, grid[nx][ny])
#             DFS(nx, ny, next_min_val, next_max_val)

# DFS(0, 0, grid[0][0], grid[0][0])
# print(ans)