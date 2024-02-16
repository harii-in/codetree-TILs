n, m, r, c = map(int, input().split())
grid = [[0] * n for _ in range(n)]

# 0초 위치
r -= 1
c -= 1
bomb_set = set()
bomb_set.add((r, c))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inRange(x, y):
    return 0 <= x < n and 0 <= y < n

# m초가 되었을 떄 격자 판에 놓여있는 폭탄의 개수
for time in range(1, m + 1):
    dist = 2 ** (time - 1)

    new = set()
    for x, y in bomb_set:
        for d in range(4):
            nx = x + dx[d] * dist
            ny = y + dy[d] * dist
            if inRange(nx, ny):
                new.add((nx, ny))
    
    bomb_set = bomb_set.union(new)

print(len(bomb_set))