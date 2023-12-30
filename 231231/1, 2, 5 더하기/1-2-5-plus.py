n = int(input())

dp = [0] * (n + 1)

# 0을 나타내는 방법은 아무것도 선택하지 않는 1가지
dp[0] = 1  

# 1부터 n까지 각 숫자에 대한 나타내는 방법의 수 계산
for i in range(1, n + 1):
    if i >= 1:
        dp[i] = (dp[i] + dp[i - 1]) % 10007
    if i >= 2:
        dp[i] = (dp[i] + dp[i - 2]) % 10007
    if i >= 5:
        dp[i] = (dp[i] + dp[i - 5]) % 10007

print(dp[n])