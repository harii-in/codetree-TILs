n = int(input())
jobs = [list(map(int, input().split())) for _ in range(n)]
dp = [job[2] for job in jobs]  # dp[i]: maximum profit when doing the i-th job

for i in range(1, n):
    for j in range(i):
        if jobs[i][0] > jobs[j][1]:
            dp[i] = max(dp[i], dp[j] + jobs[i][2])

print(max(dp))