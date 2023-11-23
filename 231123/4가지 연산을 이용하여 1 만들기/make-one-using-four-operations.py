from collections import deque

N = int(input())
visited = [0 for _ in range(1000001)]

def BFS():
    queue = deque()
    queue.append(N)
    
    while queue:
        tmp = queue.popleft()
        if visited[tmp-1] == 0:
            visited[tmp-1] = visited[tmp] + 1
            queue.append(tmp-1)
        
        if visited[tmp+1] == 0 and tmp+1<=1000001:
            visited[tmp+1] = visited[tmp] + 1
            queue.append(tmp+1)

        if tmp % 2 == 0 and visited[tmp//2] == 0:
            visited[tmp//2] = visited[tmp] + 1
            queue.append(tmp//2)
        
        if tmp % 3 == 0 and visited[tmp//3] == 0:
            visited[tmp//3] = visited[tmp] + 1
            queue.append(tmp//3)

BFS()
print(visited[1])