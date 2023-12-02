n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

# 왼쪽 상단 (1, 1)에서 출발
dp[0][0] = 1

# 아래쪽, 오른쪽으로 움직일 수 있음
# 현재 위치에서 적어도 한칸 이상 오른쪽에 있는 위치이며
# 동시에 현재 위치에서 적어도 한칸 이상 아래쪽에 있는 위치인 곳으로만 점프가 가능

# 시작 위치에서 움직일 수 있는 곳
for i in range(1, n):
    for j in range(1, m):
        if grid[0][0] < grid[i][j]:
            dp[i][j] = 2

# 한 곳씩 다 확인
for i in range(1, n-1):
    for j in range(1, m-1):
        for x in range(i+1, n):
            for y in range(j+1, m):
                if dp[i][j] != -1 and grid[i][j] < grid[x][y]:
                    dp[x][y] = max(dp[x][y], dp[i][j] + 1)

ans = 0
for i in range(1, n):
    for j in range(1, m):
        ans = max(ans, dp[i][j])

print(ans)