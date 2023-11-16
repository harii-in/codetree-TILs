import sys
sys.setrecursionlimit(50*50)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
rain = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def possible(x, y, k):
    return in_range(x, y) and not visited[x][y] and rain[x][y] > k

max_k = 1       # 최대가 되는 K(K≥1)
max_safe = 0    # 최대 안전 영역 수
def DFS(x, y, k):

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if possible(nx, ny, k):
            visited[nx][ny] = True
            DFS(nx, ny, k)

# 각 집의 높이는 1이상 100이하의 숫자
for K in range(1, 100+1):
    part = 0
    for x in range(N):
        for y in range(M):
            if possible(x, y, K):
                part += 1
                DFS(x, y, K)
    
    if max_safe < part:
        max_k = K
        max_safe = part
    
    visited = [[False]*M for _ in range(N)]

print(max_k, max_safe)