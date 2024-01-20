N = int(input())
red = [0]
blue = [0]

for i in range(1, 2 * N + 1):
    a, b = map(int, input().split())
    red.append(a)
    blue.append(b)

dp = [[0] * (N + 1) for _ in range(2 * N + 1)]
dp[0][0] = 0

for i in range(1, 2 * N + 1):
    for j in range(N + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + blue[i]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + red[i]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + red[i], dp[i - 1][j] + blue[i])

print(dp[2 * N][N])