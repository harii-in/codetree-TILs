from collections import deque
from itertools import combinations

# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y, visited):
    return in_range(x, y) and not visited[x][y]

def BFS(starts):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for x, y in starts:
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        cnt += 1

        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if possible(nx, ny, visited):
                    if u <= abs(grid[nx][ny] - grid[x][y]) <= d:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        cnt += 1
    return cnt

cities = [(x, y) for x in range(n) for y in range(n)]
max_cnt = 0
for starts in combinations(cities, k):
    max_cnt = max(max_cnt, BFS(starts))

print(max_cnt)