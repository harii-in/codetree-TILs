N, M = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (M + 1)

for i in range(N):
    w, v = jewels[i]
    for weight in range(w, M + 1):
        dp[weight] = max(dp[weight], dp[weight - w] + v)

print(dp[M])