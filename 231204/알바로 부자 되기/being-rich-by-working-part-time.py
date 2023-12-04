N = int(input())

# s는 알바가 시작되는 날짜
# e는 알바가 끝나는 날짜
# p는 해당 알바를 하여 얻을 수 있는 금액
jobs = [list(map(int, input().split())) for _ in range(N)]
# 각 날에 할 수 있는 일의 크기
dp = [job[2] for job in jobs]

for i in range(1, N):
    for j in range(i):
        if jobs[i][0] > jobs[j][1]:
            dp[i] = max(dp[i], dp[j] + jobs[i][2])

print(max(dp))