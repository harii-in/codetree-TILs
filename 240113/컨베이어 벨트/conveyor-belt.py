n, t = map(int, input().split())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

belt = upper + lower
body = belt[:-t]
move = belt[-t:]

ans = move + body
print(*ans[:n])
print(*ans[-n:])