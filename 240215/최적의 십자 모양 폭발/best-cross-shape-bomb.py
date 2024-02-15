n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(x, y):
    global temp
    bomb_size = temp[x][y]
    temp[x][y] = 0
    
    for d in range(4):
        for step in range(1, bomb_size):
            nx = x + dx[d] * step
            ny = y + dy[d] * step

            if in_range(nx, ny):
                temp[nx][ny] = 0

    # 중력 작용
    for j in range(n):
        non_zero_elements = [temp[i][j] for i in range(n) if temp[i][j] != 0]
        for i in range(n):
            if i < n - len(non_zero_elements):
                temp[n - i - 1][j] = 0  # 빈 공간을 0으로 채움
            else:
                temp[n - i - 1][j] = non_zero_elements[i - (n - len(non_zero_elements))]

def find():
    cnt = 0

    # down
    for i in range(n - 1):
        for j in range(n):
            if temp[i][j] == 0:
                continue
            if temp[i][j] == temp[i + 1][j]:
                cnt += 1
    
    # right
    for i in range(n):
        for j in range(n - 1):
            if temp[i][j] == 0:
                continue
            if temp[i][j] == temp[i][j + 1]:
                cnt += 1
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        temp = [row[:] for row in grid]
        bomb(i, j)
        ans = max(ans, find())

print(ans)