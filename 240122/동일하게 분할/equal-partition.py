n = int(input())
numbers = list(map(int, input().split()))

def can_split_equally(n, numbers):
    total = sum(numbers)

    # 가능한 모든 그룹 조합을 확인
    for i in range(1 << n):
        group_a = 0
        group_b = 0

        # 비트마스크를 이용하여 그룹 A와 그룹 B에 숫자를 나누어 할당
        for j in range(n):
            if (i & (1 << j)) > 0:
                group_a += numbers[j]
            else:
                group_b += numbers[j]

        # 두 그룹의 합이 동일한 경우 "Yes" 반환
        if group_a == group_b:
            return "Yes"

    # 모든 조합을 확인해도 동일한 합이 없는 경우 "No" 반환
    return "No"

result = can_split_equally(n, numbers)
print(result)