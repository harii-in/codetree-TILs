from itertools import combinations

n = int(input())
num_list = list(map(int, input().split()))

ans = 1e9
group1_list = [list(item) for item in combinations(num_list, n)]

for group1 in group1_list:
    group2 = [x for x in num_list if x not in group1]
    ans = min(ans, abs(sum(group1) - sum(group2)))

print(ans)