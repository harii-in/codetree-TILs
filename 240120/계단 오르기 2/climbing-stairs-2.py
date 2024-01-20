n = int(input())
coins = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = coins[i-1]
    elif i == 2:
        dp[i] = max(dp[i - 1], coins[i - 1])
    else:
        #  한 번에 1계단 오르는 것을 최대 3번까지 허용
        dp[i] = max(dp[i - 1], dp[i - 2], dp[i - 3]) + coins[i - 1]

print(dp[n])