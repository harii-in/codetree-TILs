N = int(input())
grid = [list(input()) for _ in range(N)]

#  ‘.’ (빈 공간), ‘S’ (시작점), ‘E' (도착점)
# 시작점과 도착점, 숫자 위치 저장
coins = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            continue

        if grid[i][j] == 'S':
            start = [i, j]
            continue
        elif grid[i][j] == 'E':
            end = [i, j]
            continue

        coins.append([grid[i][j], i, j])

coins.sort(key=lambda x: x[0])
def distance(f, s, t):
    dist = 0
    # x, y 계속 더하기
    # 시작에서 첫번째
    dist += abs(start[0] - f[1]) + abs(start[1] - f[2])
    # 첫번째에서 두번째
    dist += abs(f[1] - s[1]) + abs(f[2] - s[2])
    # 두번째에서 세번째
    dist += abs(s[1] - t[1]) + abs(s[2] - t[2])
    # 세번째에서 마지막
    dist += abs(t[1] - end[0]) + abs(t[2] - end[1])
    return dist

ans = 1e9
if len(coins) < 3:
    print(-1)
else:
    for i in range(len(coins)):
        first = coins[i]
        for j in range(i+1, len(coins)):
            second = coins[j]
            for k in range(j+1, len(coins)):
                third = coins[k]

                ans = min(ans, distance(first, second, third))

print(ans)