N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

while True:
    exploded = False
    to_remove = set()

    # 현재 폭탄을 기준으로 M개의 폭탄을 확인
    for i in range(N - M + 1):
        count = 1
        # 현재 폭탄을 제외한 그 다음 M-1개의 폭탄을 확인
        for j in range(1, M):
            if bombs[i + j] == bombs[i]:
                count += 1
            else:
                break
        
        # M개 이상의 연속된 숫자가 존재
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