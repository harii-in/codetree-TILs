import math
from itertools import combinations

n, m = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(n)]
location.sort(key=lambda x: x[0])

ans = 1e9
# 점 m개 선택
for points in combinations(location, m):
    # 유클리디안 거리 중 최소
    # 거리가 가장 먼 두 점의 최소 거리 -> 거리가 가장 먼 두 점의 유클라디안 거리
    distance = max((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 for p1, p2 in combinations(points, 2))
    ans = min(ans, distance)
print(int(ans))