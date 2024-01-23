N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def row_in_range(x):
    return 0 <= x < N

def move(row, direct):
    global grid

    if direct == 'L':
        last = grid[row][-1]
        grid[row][1:] = grid[row][:M-1]
        grid[row][0] = last

        direct = 'R'
    else:
        first = grid[row][0]
        grid[row][:M-1] = grid[row][1:]
        grid[row][-1] = first

        direct = 'L'
    
    return direct

def UP_move(row):
    check = False
    for col in range(M):
        if row_in_range(row - 1) and grid[row - 1][col] == grid[row][col]:
            check = True
    return check

def DOWN_move(row):
    check = False
    for col in range(M):
        if row_in_range(row + 1) and grid[row + 1][col] == grid[row][col]:
            check = True
    return check

for _ in range(Q):
    r, d = map(str, input().split())
    r = int(r) - 1

    d = move(r, d)

    up_row, down_row = r, r
    up_dir, down_dir = d, d

    while True:
        if UP_move(up_row):
            up_row -= 1
            up_dir = move(up_row, up_dir)
        else:
            break
    
    while True:
        if DOWN_move(down_row):
            down_row += 1
            down_dir = move(down_row, down_dir)
        else:
            break

for row in grid:
    print(*row)