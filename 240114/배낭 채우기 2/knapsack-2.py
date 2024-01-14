def knapsack_max_value(N, M, jewels):
    # dp 배열 초기화
    dp = [0] * (M + 1)

    # 각 보석에 대해 최대 가치 갱신
    for i in range(N):
        w, v = jewels[i]
        for weight in range(w, M + 1):
            dp[weight] = max(dp[weight], dp[weight - w] + v)

    return dp[M]

# 입력 받기
N, M = map(int, input().split())
jewels = []
for _ in range(N):
    w, v = map(int, input().split())
    jewels.append((w, v))

# 결과 출력
result = knapsack_max_value(N, M, jewels)
print(result)