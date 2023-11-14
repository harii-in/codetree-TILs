n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
visited = [False] * n

def choose(row, total):
    global ans
    if row == n:
        ans = max(ans, total)
        return

    for col in range(n):
        if visited[col]:
            continue

        visited[col] = True
        choose(row + 1, total + grid[row][col])
        visited[col] = False

choose(0, 0)
print(ans)