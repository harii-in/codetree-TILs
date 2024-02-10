# 연속된 M개의 숫자 발견 시 0으로 만들기
# 중력 작용
# 시계 방향으로 90도 회전
# 한 번 더 0으로 만들고 중력 작용
import copy

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * N for _ in range(N)]

def bomb():
    # m개 이상의 연속 수를 0으로 만들고, 중력작용하는 함수
    global IsBombed
    IsBombed = False
    while True:
        # 연속된 M개의 숫자 발견 시 0으로 만들기
        do_bomb()
        # 중력 작용
        if IsBombed:
            gravity()
            IsBombed = False
        else:
            gravity()
            break

def make_zero(start_row, end_row, col):
    for i in range(start_row, end_row + 1):
        grid[i][col] = 0

# m개 이상의 연속된 수를 0으로 만들어 터뜨리는 함수
def do_bomb():
    global IsBombed
    for j in range(N):
        num, cnt, start_idx = grid[0][j], 1, 0
        for i in range(1, N):
            if grid[i][j] == 0:
                continue
            if num == grid[i][j]:
                cnt += 1
            else:
                if cnt >= M:
                    IsBombed = True
                    make_zero(start_idx, i - 1, j)
                num, cnt, start_idx = grid[i][j], 1, i
        if cnt >= M and num != 0:
            IsBombed = True
            make_zero(start_idx, N - 1, j)

def gravity():
    global grid
    tmp = copy.deepcopy(temp)

    for j in range(N):
        last_idx = N - 1
        for i in range(N - 1, -1, -1):
            if grid[i][j]:
                tmp[last_idx][j] = grid[i][j]
                last_idx -= 1

    grid = copy.deepcopy(tmp)

def clockwise():
    global grid
    tmp = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N):
            tmp[j][N - 1 - i] = grid[i][j]
    
    grid = copy.deepcopy(tmp)
    gravity()


for _ in range(K):
    # m개 이상이면 0으로 만들고, 중력작용하기
    bomb()
    # 회전하기
    clockwise()
    # 한 번 더 0으로 만들고, 중력작용하기
    bomb()

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            ans += 1
print(ans)