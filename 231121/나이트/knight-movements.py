from collections import deque

# 8방향
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
# visited = [[False] * n for _ in range(n)]
distance = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y):
    return in_range(x, y) and distance[x][y] == 0

def BFS():
    global visited

    queue = deque()
    queue.append((r1-1, c1-1))
    # distance[r1-1][c1-1] = 0

    while queue:
        x, y = queue.popleft()

        if x == r2-1 and y == c2-1:
            return distance[x][y]


        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if possible(nx, ny):
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

    return -1

print(BFS())