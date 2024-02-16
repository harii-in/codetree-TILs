n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
flag = False
r = 0

# 블록이 떨어질 위치 찾기
for row in range(n-1, -1, -1):
    for col in range(k - 1, k - 1 + m):
        if grid[row][col] == 1:
            flag = False
            break
        elif grid[row][col] == 0:
            flag = True
    if flag:
        r = row
        break

# 블록이 떨어질 위치부터 m만큼의 영역에 블록 떨어뜨리기
if flag:
    for col in range(k - 1, k - 1 + m):
        grid[r][col] = 1

# 전체 격자판 상태 출력
for row in grid:
    print(*row)