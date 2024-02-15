n, m = map(int, input().split())
num_list = list(map(int, input().split()))
finds = list(map(int, input().split()))

cnt = dict()
for num in num_list:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

for find in finds:
    print(cnt[find] if find in cnt else 0, end=' ')