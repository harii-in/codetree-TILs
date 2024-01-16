n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find(target):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == target:
                return (i, j)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 8방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for turn in range(1, 1+m):
    # 한 번의 턴에는 숫자 1이 적힌 위치에서부터 숫자 n * n이 적힌 위치까지 순서대로 하나씩 보면서 특정 조건에 맞춰 다들 한번씩 움직임
    for num in range(1, n*n+1):
        x, y = find(num)

        neighbor = []
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if in_range(nx, ny):
                neighbor.append((grid[nx][ny], nx, ny))
        
        val, cur_x, cur_y = max(neighbor, key=lambda item: item[0])
        
        # 위치 바꾸기
        grid[x][y] = val
        grid[cur_x][cur_y] = num

for row in grid:
    print(*row)