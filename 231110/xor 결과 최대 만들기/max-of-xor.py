from itertools import combinations

n, m = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
comb = list(combinations(num, m))

for lst in comb:
    bn = lst[0]
    for n2 in lst[1:]:
        bn = bn ^ n2
    ans = max(ans, bn)

print(ans)