n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 행에 대한 행복한 수열 검사
for row in grid:
    tmp = 1
    for i in range(1, n):
        if row[i] == row[i-1]:
            tmp += 1
            if tmp >= m:
                ans += 1
                continue
        else:
            tmp = 1

# 열에 대한 행복한 수열 검사
for j in range(n):
    tmp = 0
    for i in range(1, n):
        if grid[i][j] == grid[i-1][j]:
            tmp += 1
            if tmp >= m:
                ans += 1
                continue
        else:
            tmp = 1

if m == 1:
    print(n*2)
else:
    print(ans)