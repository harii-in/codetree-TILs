n, t = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
under = list(map(int, input().split()))

belt = left + right + under

for _ in range(t):
    temp = belt[-1]
    belt[1:] = belt[:-1]
    belt[0] = temp

print(*belt[:n])
print(*belt[n:2*n])
print(*belt[2*n:])