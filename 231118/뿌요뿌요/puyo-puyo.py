# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def possible(x, y, k):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == k

block = 0           # 최대 블럭의 크기
bomb_block = 0      # 터지게 되는 블럭의 수

tmp = 0
def DFS(x, y, k):
    global tmp

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if possible(nx, ny, k):
            visited[nx][ny] = True

            tmp += 1
            DFS(nx, ny, k)

for x in range(n):
    for y in range(n):
        if possible(x, y, grid[x][y]):
            visited[x][y] = True
            tmp = 1
            DFS(x, y, grid[x][y])

            block = max(block, tmp)
            if tmp >= 4:
                bomb_block += 1

print(bomb_block, block)