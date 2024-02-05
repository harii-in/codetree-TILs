import copy

grid = [list(map(int, input().split())) for _ in range(4)]
dir = input()

def up(board):
    for j in range(4):
        cursor = 0
        for i in range(4):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp

                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1

                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board


def clockwise(lst):
    return list(map(list, zip(*lst[::-1])))

copy_grid = copy.deepcopy(grid)
if dir == 'L':
    grid = clockwise(grid)
    grid = up(grid)
    for _ in range(3):
        grid = clockwise(grid)

elif dir == 'R':
    for _ in range(3):
        grid = clockwise(grid)
    grid = up(grid)
    grid = clockwise(grid)

elif dir == 'D':
    for _ in range(2):
        grid = clockwise(grid)
    grid = up(grid)
    for _ in range(2):
        grid = clockwise(grid)

else:
    grid = up(grid)


for i in range(4):
    print(*grid[i])