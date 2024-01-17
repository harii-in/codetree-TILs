n = int(input())
blocks = [int(input()) for _ in range(n)]

def remove_blocks(start, end):
    return blocks[:start] + blocks[end+1:]

# 첫 번째 제거 작업
s1, e1 = map(int, input().split())
blocks = remove_blocks(s1-1, e1-1)

# 두 번째 제거 작업
s2, e2 = map(int, input().split())
blocks = remove_blocks(s2-1, e2-1)

print(len(blocks))
for block in blocks:
    print(block)