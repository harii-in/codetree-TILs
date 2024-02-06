n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

x, y = r - 1, c - 1
compare = grid[x][y]
visited = [compare]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

def move():
    global x, y, compare
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if inRange(nx, ny) and grid[nx][ny] > compare:
            compare = grid[nx][ny]
            x, y = nx, ny
            return True
    return False

while move():
    visited.append(grid[x][y])

print(*visited)