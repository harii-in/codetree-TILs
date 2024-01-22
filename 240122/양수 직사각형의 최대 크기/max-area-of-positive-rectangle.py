n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

rect_list = []
for start_row in range(n):
    for end_row in range(start_row, n):
        for start_col in range(m):
            for end_col in range(start_col, m):
                rect = [[0] * m for _ in range(n)]
                for row in range(start_row, end_row + 1):
                    for col in range(start_col, end_col + 1):
                        rect[row][col] = 1
                
                rect_list.append(rect)

def sum_grid_rect(rect):
    return sum([
        grid[row][col]
        for col in range(m)
        for row in range(n)
        if rect[row][col]
    ])

def is_positive(rect):
    cnt = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] <= 0 and rect[row][col]:
                return False
            if rect[row][col]:
                cnt += 1
    return cnt

ans = -1
limit = len(rect_list)
for idx in range(limit):
    rect = rect_list[idx]
    
    tmp = is_positive(rect)
    if not tmp:
        continue

    ans = max(ans, tmp)

print(ans)