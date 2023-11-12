import copy
from itertools import combinations

n = int(input())
num_list = list(map(int, input().split()))

ans = 1e9
group1_list = [list(item) for item in combinations(num_list, n)]

for group1 in group1_list:
    group2 = copy.deepcopy(num_list)
    for item in group1:
        group2.remove(item)
    ans = min(ans, abs(sum(group1) - sum(group2)))

print(ans)