N, M = map(int, input().split())

# w는 해당 보석의 무게,  v는 해당 보석의 가치
gems = [tuple(map(int,input().split())) for _ in range(N)]
dp = [0] * (M+1)

for i in range(N):
    w, v = gems[i]
    # j를 배낭의 최대 무게 M에서 보석의 무게 w까지 보석을 배낭에 넣을 수 있는지 확인
    # w가 M보다 크면 아무런 숫자를 생성 x → 보석은 배낭에 들어갈 수 없음
    for j in range(M, w-1, -1):
        # 보석을 넣지 않았을 때의 가치와 보석을 넣었을 때의 가치 비교
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[-1])