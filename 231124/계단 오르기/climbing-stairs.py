MOD = 10007
# 2 ≤ n ≤ 1,000
n = int(input())

dp = [0]*(1001)

# 1층을 올라갈 방법이 X
dp[1] = 0

# 2층을 올라갈 방법
dp[2] = 1

# 3층을 올라갈 방법
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = (dp[i - 3] + dp[i - 2]) % MOD

print(dp[n])