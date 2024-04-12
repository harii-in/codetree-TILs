# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

L, N, Q = map(int, input().split())
# 0이라면 빈칸을 의미
# 1이라면 함정을 의미
# 2라면 벽을 의미
grid = [[2]*(N+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2]*(N+2)]
visited = [[0]*(N+2) for _ in range(N+2)]

# 초기 기사들의 정보
knight = {}
life = [0] * (N+1)
for n in range(1, N+1):
    r,c,h,w,k = map(int, input().split())
    knight[n] = [r, c, h, w, k]
    life[n] = k

    for i in range(r, r+h):
        visited[i][c:c+w] = [n]*w

def push_unit(start, d):
    queue = []
    pset = set()
    damage = [0] * (N+1) 

    queue.append(start)
    pset.add(start)

    while queue:
        tmp = queue.pop(0)
        r, c, h, w, k = knight[tmp]

        nx = r + dx[d]
        ny = c + dy[d]
        for x in range(nx, nx+h):
            for y in range(ny, ny+w):
                if grid[x][y] == 2:
                    return
                if grid[x][y] == 1:
                    # 함정인 경우 데미지
                    damage[tmp] += 1

        for idx in knight:
            if idx in pset:
                continue
            
            tr, tc, th, tw, tk = knight[idx]
            if nx <= tr+th-1 and nx+h-1 >= tr and tc <= ny+w-1 and ny <= tc+tw-1:
                queue.append(idx)
                pset.add(idx)

    damage[start] = 0

    # 체력 소진시 사라짐
    for idx in pset:
        r, c, h, w, k = knight[idx]

        if k <= damage[idx]:
            knight.pop(idx)
        else:
            nx = r + dx[d]
            ny = c + dy[d]
            knight[idx] = [nx, ny, h, w, k-damage[idx]]


# 왕의 명령
for _ in range(Q):
    i, d = map(int, input().split())
    if i in knight:
        # 기사 이동
        push_unit(i, d)

ans = 0
for idx in knight:
    ans += life[idx] - knight[idx][4]
print(ans)