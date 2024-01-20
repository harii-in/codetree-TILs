n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def calPrice(k):
    return k * k + (k + 1) * (k + 1)

def cntGold(x, y, k):
    total = 0
    for i in range(n):
        for j in range(n):
            # 마름모 계산
            if abs(x - i) + abs(y - j) <= k:
                total += grid[i][j]
    return total

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n+1):
            tmp = cntGold(i, j, k)
            if (tmp * m) >= calPrice(k) and ans < tmp:
                ans = tmp

print(ans)