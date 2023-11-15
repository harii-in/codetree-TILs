n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

lst = []
ans = 0
def count(cnt):
    global lst, ans
    if cnt == n:
        total = min(lst)
        ans = max(ans, total)
        return

    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        lst.append(grid[cnt][i])

        count(cnt + 1)

        visited[i] = False
        lst.pop()

count(0)       
print(ans)