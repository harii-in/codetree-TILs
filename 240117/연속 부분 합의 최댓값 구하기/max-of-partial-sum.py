n = int(input())
arr = list(map(int, input().split()))

max_sum = current_sum = arr[0]

for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)