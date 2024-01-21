N, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [[0] * 41 for _ in range(N + 1)]

dp[0][lst[0] + 20] = 1
dp[0][(-1) * lst[0] + 20] += 1

for i in range(1, N):
    for j in range(-20, 21):
        if -20 <= j + lst[i] <= 20:
            dp[i][j + 20 + lst[i]] += dp[i - 1][j + 20]
        if -20 <= j - lst[i] <= 20:
            dp[i][j + 20 - lst[i]] += dp[i - 1][j + 20]

print(dp[N-1][M+20])