n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def RowColSum(seq):
    result = 0
    for i in seq:
        result += i
    return result

def square(row, col):
    area, min_cell = 0, float('inf')
    for i in range(row, row+2):
        for j in range(col, col+2):
            min_cell = min(min_cell, grid[i][j])
            area += grid[i][j]
    return area - min_cell
    
# row
for row in range(n):
    for col in range(m):
        if col + 2 >= m:
            continue
        
        ans = max(ans, RowColSum(grid[row][col:col+3]))

# col
for col in range(m):
    for row in range(n):
        if row + 2 >= n:
            continue
        lst = []
        for i in range(row, row+3):
            lst.append(grid[i][col])
        ans = max(ans, RowColSum(lst))

for row in range(n):
    for col in range(m):
        if row + 1 >= n or col + 1 >= m:
            continue
        ans = max(ans, square(row, col))

print(ans)