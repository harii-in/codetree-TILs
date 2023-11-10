n = int(input())
# 각 위치는 최대 점프 가능 거리
pos_jump = list(map(int, input().split()))

jump = [1e9]*n

jump[0] = 0     # 첫 번째 위치로부터 n번째 위치에 도달하기 위해 필요한 최소 점프 횟수이므로
# 처음 위치에서 최대한 점프 할 수 있는 곳까지 1로 설정
for i in range(1, pos_jump[0]+1):
    if i>=n:
        break
    jump[i] = 1

# 두 번째 위치부터 탐색.
# 탐색 시 각 위치에서 최대 점프 가능 거리 고려.
for i in range(1, n):
    for j in range(i+1, i+pos_jump[i]+1):
        # 점프 한게 범위 넘어가는지
        if j >= n:
            break
        # 현재 위치까지의 최소 점프 수와 업데이트한 점프 수 비교 후 작은 것 선택
        jump[j] = min(jump[j], jump[i] + 1)

print(jump[-1] if jump[-1] != 1e9 else -1)