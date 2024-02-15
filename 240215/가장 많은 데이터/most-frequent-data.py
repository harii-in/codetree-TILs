n = int(input())
counter = dict()

for _ in range(n):
    string = input()
    if string in counter:
        counter[string] += 1
    else:
        counter[string] = 1

print(max(counter.values()))