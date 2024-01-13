n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 동전의 수
ans = 0

for i in range(n-2):
    for j in range(n-2):
        coin = sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3])
        ans = max(ans, coin)

print(ans)