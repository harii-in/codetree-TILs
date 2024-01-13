n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

for _ in range(t):
    temp = upper[-1]
    upper[1:] = upper[:-1]
    upper[0] = lower[-1]
    lower[1:] = lower[:-1]
    lower[0] = temp

print(*upper)
print(*lower)