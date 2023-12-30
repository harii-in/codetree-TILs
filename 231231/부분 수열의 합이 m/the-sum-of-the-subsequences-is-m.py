# 수열 A의 원소의 개수 n과 만들고자 하는 합 m
n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [1e9]*(m+1)
dp[0] = 0

# 각 수 선택
for i in range(n):
    # 합 j를 만들기 위해
    # i번 원소를 사용한 경우에 대해 업데이트
    # 각 원소를 최대 한 번씩만 사용하기 위해
    # 포문을 0 -> m이 아닌, m -> 0 방향으로 진행
    for j in range(m, -1, -1):
        if j >= A[i]:
            dp[j] = min(dp[j], dp[j - A[i]] + 1)

if dp[m] == 1e9:
    print(-1)
else:
    print(dp[m])