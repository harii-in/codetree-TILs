n = int(input())
town = [list(map(int, input().split())) for _ in range(n)]
visited =[[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def possible(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or town[x][y] == 0:
        return False

    return True

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp = 0
town_people = []
def DFS(x, y):
    global tmp

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if possible(nx, ny):
            visited[nx][ny] = True

            tmp += 1
            DFS(nx, ny)

for x in range(n):
    for y in range(n):
        if possible(x, y):
            visited[x][y] = True
            tmp = 1
            DFS(x, y)
            town_people.append(tmp)

town_people.sort()
print(len(town_people))
for x in town_people:
    print(x)