from collections import deque

n = int(input())
lst = deque(list(map(int, input().split())))

queue = deque()

num = lst.popleft()

# 현재 수를 그룹 A에 포함
# 양수의 경우가 그룹 A
queue.append(num)

# 현재 수를 그룹 B에 포함
# 음수의 경우가 그룹 B
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