n = int(input())
jump = list(map(int, input().split()))

dp = [-1] * n
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        if dp[j] == -1:
            continue
        if jump[j] >= i - j:
            dp[i] = max(dp[i], dp[j] + 1)

max_jump = max([x for x in dp if x != -1])
print(max_jump)