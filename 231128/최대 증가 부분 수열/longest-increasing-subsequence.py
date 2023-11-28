N = int(input())
num = list(map(int, input().split()))
dp = [0] * N

ans = 0
for i in range(1, N):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)+1)