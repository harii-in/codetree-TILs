n, m = map(int, input().split())
num_to_str = dict()
str_to_num = dict()

for i in range(1, n + 1):
    s = input()
    num_to_str[i] = s
    str_to_num[s] = i

for _ in range(m):
    query = input()
    # 문자열이 '숫자'로만 이루어져있는지 확인하는 함수
    if query.isdigit():
        print(num_to_str[int(query)])
    else:
        print(str_to_num[query])