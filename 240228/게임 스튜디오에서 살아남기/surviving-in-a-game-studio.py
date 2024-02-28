import itertools

n = int(input())

temp = itertools.product("GBT", repeat=n)
arr = list(map(''.join, list(temp)))

cnt = 0
for i in arr:
    if i.count("T") >=3 or "BBB" in i:
        cnt += 1

temp = len(arr) - cnt
print(temp % (10**9 + 7))