from copy import deepcopy
from collections import deque
from itertools import combinations
# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, k, m = map(int, input().split())
grid = []

stones = []  # 돌 위치
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(n):
        # 숫자 1은 돌이 있어 해당 칸이 이동할 수 없는 곳
        if row[j] == 1:
            stones.append((i, j))

starts = [] # 시작 위치
for _ in range(k):
    i, j = map(int, input().split())
    # visited 대신 움직였는지 확인 위해 2로 처리
    grid[i-1][j-1] = 2
    starts.append((i-1, j-1))

def BFS(removed_stones):
    new_grid = deepcopy(grid)
    # new_grid = [row[:] for row in grid]
    for x, y in remove_stones:
        new_grid[x][y] = 0

    queue = deque(starts)

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n):  # nx, ny를 검사
                continue

            if not new_grid[nx][ny] == 0:  # new_grid의 nx, ny 위치를 검사
                continue

            queue.append((nx, ny))
            new_grid[nx][ny] = 2


    cnt = sum(1 for i in range(n) for j in range(n) if new_grid[i][j] == 2)
    return cnt

max_cnt = 0
for remove_stones in combinations(stones, m):
    max_cnt = max(max_cnt, BFS(remove_stones))

print(max_cnt)