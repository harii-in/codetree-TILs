n = int(input())
hashmap = dict()

for _ in range(n):
    tmp = input().split()

    if tmp[0] == "add":
        hashmap[tmp[1]] = tmp[2]

    elif tmp[0] == "remove":
        del hashmap[tmp[1]]

    elif tmp[0] == "find":
        print(hashmap[tmp[1]] if tmp[1] in hashmap else "None")