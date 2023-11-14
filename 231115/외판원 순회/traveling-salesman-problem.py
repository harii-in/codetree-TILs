n = int(input())
exp = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9
visited = [False] * n
visited[0] = True

# row와 cnt는 엄연히 다름
def move(cnt, row, total):
    global ans
    # 1번 지점으로 돌아오는 경우
    if cnt == n-1:
        if exp[row][0] == 0:
            return
        ans = min(ans, total + exp[row][0])
        return

    for col in range(n):
        if visited[col] or exp[row][col] == 0:
            continue
        
        visited[col] = True
        move(cnt+1, col, total + exp[row][col])
        visited[col] = False

move(0, 0, 0)
print(ans)