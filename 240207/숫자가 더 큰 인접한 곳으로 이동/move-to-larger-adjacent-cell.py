n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

cur_x, cur_y = r - 1, c - 1
compare_num = arr[cur_x][cur_y]
visited_arr = [compare_num]

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move():
    global cur_x, cur_y, compare_num
    for dx, dy in zip(dxs, dys):
        next_x, next_y = cur_x + dx, cur_y + dy
        if is_in_range(next_x, next_y) and arr[next_x][next_y] > compare_num:
            compare_num = arr[next_x][next_y]
            cur_x, cur_y = next_x, next_y
            return True

    return False

while move():
    visited_arr.append(arr[cur_x][cur_y])

print(*visited_arr)