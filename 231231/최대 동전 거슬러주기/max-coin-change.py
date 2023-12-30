N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [-1] * (M + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, M + 1):
        if dp[i - coin] != -1:
            dp[i] = max(dp[i], dp[i - coin] + 1)

print(dp[M])