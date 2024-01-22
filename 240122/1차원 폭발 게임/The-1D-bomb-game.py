N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

while True:
    exploded = False
    to_remove = set()

    for i in range(N - M + 1):
        count = 1
        for j in range(1, M):
            if bombs[i + j] == bombs[i]:
                count += 1
            else:
                break
        if count >= M:
            for j in range(M):
                to_remove.add(i + j)
            exploded = True

    if exploded:
        bombs = [bombs[i] for i in range(N) if i not in to_remove]
        N = len(bombs)
    else:
        break

print(N)
for num in bombs:
    print(num)