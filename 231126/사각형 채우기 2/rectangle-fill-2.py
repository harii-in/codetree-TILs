MOD = 10007
MAX_NUMBER = 1001

n = int(input())
dp = [0] * MAX_NUMBER

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

print(dp[n])