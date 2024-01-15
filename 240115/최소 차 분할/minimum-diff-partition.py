from collections import deque

n = int(input())
lst = deque(list(map(int, input().split())))

queue = deque()

num = lst.popleft()
queue.append(num)
queue.append(-num)

while lst:
    num = lst.popleft()
    group = set()
    while queue:
        tmp = queue.popleft()
        group.add(tmp + num)
        group.add(tmp - num)
    queue = deque(group)

print(min(map(abs, queue)))