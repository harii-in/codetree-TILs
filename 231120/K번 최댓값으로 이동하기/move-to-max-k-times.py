from collections import deque
# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 시작 위치
r, c = map(int, input().split())
r -= 1
c -= 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y, sx, sy):
    return in_range(x, y) and not visited[x][y] and grid[x][y] < grid[sx][sy]


# 최댓값, 다음 번 위치

def BFS(xx, yy):
    queue = deque()
    queue.append((xx, yy))
    visited[xx][yy] = True

    max_num = 0
    max_pos = (xx, yy)
    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if possible(nx, ny, xx, yy):
                queue.append((nx, ny))
                visited[nx][ny] = True

                if grid[nx][ny] > max_num:
                    max_num = grid[nx][ny]
                    max_pos = (nx, ny)

                elif grid[nx][ny] == max_num:
                    if max_pos[0] > nx:
                        max_pos = (nx, ny)
                    elif max_pos[0] == nx:
                        if max_pos[1] > ny:
                            max_pos = (nx, ny)

    return max_pos

for _ in range(k):
    visited = [[False]*n for _ in range(n)]
    r, c = BFS(r, c)

print(r+1, c+1)