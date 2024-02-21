n, k = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
sum_dict = dict()
for num in num_list:
    complement = k - num

    if complement in sum_dict:
        cnt += sum_dict[complement]

    if num in sum_dict:
        sum_dict[num] += 1
    else:
        sum_dict[num] = 1

print(cnt)