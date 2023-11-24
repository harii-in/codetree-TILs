# 가능한 모든 루트 노드에 대해
# 독립된 사건인 왼쪽 BST의 경우의 수와 오른쪽 BST의 경우의 수를 곱해줌으로써 모든 경우의 수를 구할 수 있음

N = int(input())

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    total = 0

    for j in range(N+1):
        total += dp[j] * dp[i-j-1]

    dp[i] = total

print(dp[N])