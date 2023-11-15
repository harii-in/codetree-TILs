from collections import defaultdict

N, M = map(int, input().split())
edges = defaultdict(list)
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

def DFS(v):
    visited[v] = True
    for i in edges[v]:
        if not visited[i]:
            DFS(i)

# 1번 정점에서 시작
DFS(1)
# 1번 정점 자기 자신에 도달하는 경우는 가지수에서 제외
print(visited.count(True)-1)