n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = {}
for num in nums:
    if num not in count:
        count[num] = 1
    else:
        count[num] += 1

# -x[1]은 빈도수를 기준으로 내림차순 정렬하겠다는 의미
# -x[0]는 빈도수가 같을 경우 숫자를 기준으로 내림차순 정렬하겠다는 의미
sorted_nums = sorted(count.items(), key=lambda x: (-x[1], -x[0]))

for i in range(k):
    print(sorted_nums[i][0], end=' ')