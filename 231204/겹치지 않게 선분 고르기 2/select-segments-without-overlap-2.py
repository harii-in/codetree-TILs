n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

choices = []
max_choice = 0

def choice_line(depth):
    global max_choice
    max_choice = max(max_choice, len(choices))

    for i in range(depth, n):
        if is_overlapped(lines[i]):
            continue
        choices.append(lines[i])
        choice_line(i + 1)
        choices.remove(lines[i])

def is_overlapped(line):
    for choice in choices:
        if choice[0] == line[0] or choice[1] == line[1]:
            return True
        if choice[0] > line[0] and choice[1] > line[1]:
            continue
        if choice[0] < line[0] and choice[1] < line[1]:
            continue
        return True
    return False

choice_line(0)
print(max_choice)