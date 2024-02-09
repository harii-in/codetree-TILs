A = input()
n = len(A)

def encode(target):
    encoded = ""
    encoded += target[0]
    cnt = 1

    for i in range(1, len(target)):
        if target[i] == target[i - 1]:
            cnt += 1
            continue
        encoded += str(cnt)
        encoded += target[i]
        cnt = 1

    encoded += str(cnt)

    return encoded

def shift(target, cnt):
    return target[cnt:] + target[:cnt]


min_len = 1e9
old = A

for cnt in range(1, n):
    shifted = shift(old, 1)
    encoded = encode(shifted)
    min_len = min(min_len, len(encoded))
    old = shifted

if n == 1:
    print(2)
else:
    print(min_len)