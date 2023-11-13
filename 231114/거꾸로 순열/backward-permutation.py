from itertools import permutations

n = int(input())
perm = list(permutations([x for x in range(1, n+1)]))
perm.sort(reverse = True)

for p in perm:
    print(' '.join(map(str, p)))