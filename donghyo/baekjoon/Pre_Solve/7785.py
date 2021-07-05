name = {}
n = int(input())

for _ in range(n):
    a, event = map(str, input().split())

    if event == 'enter':
        name[a] = 'enter'
    else:
        if name[a]:
            del name[a]

for i in sorted(name, reverse= True): print(i)
