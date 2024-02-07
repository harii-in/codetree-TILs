# 바라보고 있는 방향으로 이동 불가능 -> 반시계 90도
# 바라보는 방향으로 이동 가능한 경우
# 바로 앞이 격자 밖이면 탈출
# 오른쪽에 벽 있으면 직진
# 직진 했는데 오른쪽에 벽 없으면 시계방향으로 90도 회전후 한 칸 전진

N = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1

# 해당 위치에 벽이 있는 경우에는 ‘#' 문자가, 벽이 없다면 '.’ 
grid = [list(input()) for _ in range(N)]

# 동, 서, 남, 북 <- 우측 방향 바라보고 시작
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

direction = 0
def move():
    global direction
    tmp = 0     # 사방 막혔는지 확인(네 방향 다 확인했는가)
    for d in range(4):
        tmp += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if inRange(nx, ny):
            # 진행방향에 벽?
            if grid[nx][ny] == '#':
                direction = (direction + 3) % 4
            # 진행방향에 벽X
            elif grid[nx][ny] == '.':
                break   # 움직여
        else:
            return (-1, -1)
    return (nx, ny) if tmp != 4 else (x, y)

def checkRight():
    right = (direction + 1) % 4
    nx, ny = x + dx[right], y + dy[right]

    # 오른쪽에 벽이 있는 경우
    if grid[nx][ny] == '#':
        return True
    # 오른쪽에 벽이 없는 경우
    else:
        return False

ans = 0
for _ in range(N * N):
    # 진행하기
    pos = move()
    ans += 1
    
    # 밖으로 나갔다면 반복 종료
    if pos == (-1, -1):
        break
    
    x, y = pos
    # 진행 방향 기준 오른쪽에 벽 유무 확인
    # 벽이 없다면 진행방향 바꾸기
    if not checkRight():
        direction = (direction + 1) % 4

print(ans if ans != N * N else -1)