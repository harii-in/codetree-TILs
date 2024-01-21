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

def is_intersect(rect1, rect2):
    for row in range(n):
        for col in range(m):
            if rect1[row][col] and rect2[row][col]:
                return True
    return False


ans = -1e9
limit = len(rect_list)
for idx_rect1 in range(limit - 1):
    for idx_rect2 in range(idx_rect1 + 1, limit):
        rect1 = rect_list[idx_rect1]
        rect2 = rect_list[idx_rect2]
        
        if is_intersect(rect1, rect2):
            continue
        rect_sum = sum_grid_rect(rect1) + sum_grid_rect(rect2)

        ans = max(ans, rect_sum)

print(ans)