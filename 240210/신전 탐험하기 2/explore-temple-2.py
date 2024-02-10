n = int(input())
dia = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    for j in range(3):
        if i == 0:
            dp[i][j] = dia[i][j]
        else:
            for k in range(3):
                if j != k:
                    dp[i][j] = max(dp[i][j], dp[i - 1][k] + dia[i][j])

print(max(dp[n - 1]))