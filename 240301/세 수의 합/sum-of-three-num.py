from itertools import combinations

n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for three in combinations(nums, 3):
    if sum(three) == k:
        ans += 1

print(ans)