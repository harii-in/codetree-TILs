from collections import deque
# 상, 하, 좌, 우
dx = [1, 0]
dy = [0, 1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def DFS(x, y):
    if x == n-1 and y == n-1:
        return grid[x][y]

    if visited[x][y]:
        return visited[x][y]

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if in_range(nx, ny):
            visited[x][y] = max(visited[x][y], DFS(nx, ny) + grid[x][y])
            
    return visited[x][y]

print(DFS(0, 0))