import copy
from collections import deque

def inRange(x, y, RR):
    global C
    return 0 <= x < RR and 0 <= y < C

# 반시계 90도 회전
def leftclock(arr):
    return list(map(list, zip(*arr)))[::-1]

# 시계 90도 회전
def rightclock(arr):
    return list(map(list, zip(*arr[::-1])))

golem = [
    [0, 1, 0],
    [1, 3, 1], 
    [0, 1, 0]
    ]

# 하, 좌, 우, 상
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

# golem이 grid 상에서 겹치는지 확인
def check_golem(x, y):
    global grid, R
    if grid[x][y] == 0:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not inRange(nx, ny, R+3) or grid[nx][ny] != 0:
                return False
    else:
        return False
    return True

def gravity(col, E):
    global grid

    # 출구 방향 E: 0,1,2,3은 북, 동, 남, 서쪽을 의미
    tmp = copy.deepcopy(golem)
    if E == 0:
        tmp[0][1] = 2
    elif E == 1:
        tmp[1][2] = 2
    elif E == 2:
        tmp[2][1] = 2
    elif E == 3:
        tmp[1][0] = 2
    
    row = 1
    while True:
        # 아래로 이동
        if check_golem(row+1, col):
            row += 1
            continue

        # 반시계
        if check_golem(row, col-1):
            if check_golem(row+1, col-1):
                tmp = leftclock(tmp)
                row += 1
                col -= 1
                continue

        # 시계
        if check_golem(row, col+1):
            if check_golem(row+1, col+1):
                tmp = rightclock(tmp)
                row += 1
                col += 1
                continue
        
        # 셋 다 아니면
        break

    # 상위 3행에 걸쳐져 있으면 범위를 벗어난 것이므로 끝
    if row < 4:
        return (-1, -1)
    
    # 중력 다 받으면 grid에 적용
    grid[row][col] = tmp[1][1]
    for d in range(4):
        grid[row + dx[d]][col + dy[d]] = tmp[1 + dx[d]][1 + dy[d]]

    # golem 중앙 반환 -> score 계산 위해
    return (row, col)

def move(row, col):
    global grids, R, C
    visited = [[0]*C for _ in range(R)]

    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1

    ans = 0     # 정령이 움직일 수 있는 최대 row
    while queue:
        x, y = queue.popleft()

        # 중앙, 출구에서는 어디든지 이동 가능
        if grids[x][y] == 2 or grids[x][y] == 3:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if inRange(nx, ny, R) and grids[nx][ny] != 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    ans = max(ans, nx)
        
        # 중앙도 출구도 아니라면 중앙으로만 이동
        elif grids[x][y] == 1:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if inRange(nx, ny, R) and grids[nx][ny] == 3 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    ans = max(ans, nx)
    # print(visited)
    return ans

R, C, K = map(int, input().split())

score = 0
grid = [[0]*C for _ in range(R+3)]
for _ in range(K):
    col, E = map(int, input().split())
    col -= 1

    # golem 중력
    x, y = gravity(col, E)

    # 범위를 벗어난 경우 reset
    if (x, y) == (-1, -1):
        grid = [[0]*C for _ in range(R+3)]
        continue

    x -= 3
    grids = grid[3:]
    # print('grid', grid)
    # print('grids', grids)
    score += (move(x, y) + 1)   # 문제에서 (1, 1)이 좌측 상단이기 때문
    # print('점수', score)

print(score)