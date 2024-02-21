n, k = map(int, input().split())
num_list = list(map(int, input().split()))

cnt = 0
sum_dict = dict()
for num in num_list:
    complement = k - num

    # 가능한 모든 쌍의 수 세기
    if complement in sum_dict:
        cnt += sum_dict[complement]

    # 현재 숫자의 개수 하나 증가
    if num in sum_dict:
        sum_dict[num] += 1
    else:
        sum_dict[num] = 1

print(cnt)