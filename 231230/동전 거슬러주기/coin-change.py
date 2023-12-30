# N개의 동전의 종류, 금액 M
N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [1e9] * (M+1)

# 0원
dp[0] = 0

for coin in coins:
    for n in range(coin, M+1):
        dp[n] = min(dp[n], dp[n - coin] + 1)

if dp[M] == 1e9:
    print(-1)
else:
    print(dp[M])