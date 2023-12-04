N, M = map(int, input().split())

# w는 해당 보석의 무게,  v는 해당 보석의 가치
gems = [tuple(map(int,input().split())) for _ in range(N)]
dp = [0] * (M+1)

for i in range(N):
    w, v = gems[i]
    for j in range(M, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[-1])