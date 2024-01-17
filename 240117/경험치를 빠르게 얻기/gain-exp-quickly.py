n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

dp = [-1] * (m + 1)
dp[0] = 0

# 각 퀘스트로 부터 얻은 경험치의 총 합이 m 이상이며 걸리는 총 시간이 최소가 되도록
for e, t in quests:
    for j in range(m, e - 1, -1):
        if dp[j - e] != -1:
                if dp[j] == -1 or dp[j - e] + t < dp[j]:
                    dp[j] = dp[j - e] + t
print(dp[m])