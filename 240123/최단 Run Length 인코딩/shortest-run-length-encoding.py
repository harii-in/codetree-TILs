A = list(input())

def run_length_encoding(s):
    result = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result

ans = ''
ans_len = float('inf')
for _ in range(len(A)):
    last = A.pop(0)
    A.append(last)

    tmp = run_length_encoding(''.join(A))
    if ans_len > len(tmp):
        ans_len = len(tmp)
        ans = tmp

print(ans_len)