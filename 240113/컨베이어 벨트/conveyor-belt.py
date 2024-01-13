n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

belt = upper + lower

for _ in range(t):
    temp = belt[-1]
    belt[1:] = belt[:-1]
    belt[0] = temp

print(*belt[:n])
print(*belt[n:])