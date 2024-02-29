from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = defaultdict(int)
CD = defaultdict(int)

for a in A:
    for b in B:
        AB[a+b] += 1

for c in C:
    for d in D:
        CD[c+d] += 1

ans = 0
for ab in AB:
    if -ab in CD:
        ans += AB[ab] * CD[-ab]

print(ans)