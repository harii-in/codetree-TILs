from itertools import combinations

N, M = map(int, input().split())

comb = list(combinations([x for x in range(1, N+1)], M))

for pair in comb:
    print(' '.join(map(str, pair)))