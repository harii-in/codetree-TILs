N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def makeZero(startRow, endRow, col):
    for i in range(startRow, endRow + 1):
        grid[i][col] = 0

def Bomb():
    global IsBombed

    for j in range(N):
        curNum, curCnt, startIdx = grid[0][j], 1, 0
        for i in range(1, N):
            if grid[i][j] == 0:
                continue

            if curNum == grid[i][j]:
                curCnt += 1
            else:
                if curCnt >= M:
                    IsBombed = True
                    makeZero(startIdx, i - 1, j)
                curNum, curCnt, startIdx = grid[i][j], 1, i

        if curCnt >= M and curNum != 0:
            IsBombed = True
            makeZero(startIdx, N - 1, j)

def InitializeTmp():
    global temp
    temp = [[0] * N for _ in range(N)]

def Gravity():
    InitializeTmp()

    for j in range(N):
        tempLastIdx = N - 1
        for i in range(N - 1, -1, -1):
            if grid[i][j]:
                temp[tempLastIdx][j] = grid[i][j]
                tempLastIdx -= 1

    for i in range(N):
        for j in range(N):
            grid[i][j] = temp[i][j]

def FindStraightNumbers():
    global IsBombed
    
    IsBombed = False
    while True:
        Bomb()
        if IsBombed:
            Gravity()
            IsBombed = False
        else:
            Gravity()
            break

def ClockWise():
    global grid
    grid = list(map(list, zip(*grid[::-1])))

for _ in range(K):
    FindStraightNumbers()
    ClockWise()
    FindStraightNumbers()

ans = 0
for row in grid:
    ans += sum(row)

print(ans)