from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = defaultdict(int)
CD = defaultdict(int)

# A 수열에서 숫자 하나, B 수열에서 숫자 하나를 골랐을 때
# 나올 수 있는 두 숫자의 합들을 hashmap에 기록해줍니다.
for a in A:
    for b in B:
        AB[a+b] += 1

# C, D도 마찬가지
for c in C:
    for d in D:
        CD[c+d] += 1

ans = 0
for ab in AB:
    # CD에 -ab가 몇 개 들어 있는지를 찾기
    if -ab in CD:
        ans += AB[ab] * CD[-ab]

print(ans)