n, m, r, c = map(int, input().split())
direction = list(input().split())

# 왼쪽, 오른쪽, 위, 아래
# ‘L', ‘R’, ‘U’, 'D’
coord = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}
grid = [[0] * n for _ in range(n)]

# 주사위
dice = [
    [0, 5, 0],
    [4, 6, 3],
    [0, 2, 0]
]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def roll(d):
    global dice

    mid = dice[1][1]
    if d == 'L':
        dice[1] = [7 - mid, dice[1][0], dice[1][1]]
    elif d == 'R':
        dice[1] = [dice[1][1], dice[1][2], 7 - mid]
    elif d == 'U':
        [dice[0][1], dice[1][1], dice[2][1]] = [7 - mid, dice[0][1], dice[1][1]]
    elif d == 'D':
        [dice[0][1], dice[1][1], dice[2][1]] = [dice[1][1], dice[2][1], 7 - mid]

x = r-1
y = c-1
grid[x][y] = dice[1][1]     # 시작 좌표에 현재 값 추가
for d in direction:
    dx, dy = coord[d]

    nx = x + dx
    ny = y + dy

    if inRange(nx, ny):
        x = nx
        y = ny
        roll(d)
        grid[x][y] = dice[1][1]

ans = 0
for row in grid:
    ans += sum(row)

print(ans)