N = int(input())
stack = []
res = []

for i in range(N):
    command = str(input())
    go = command.split(" ")

    if len(go) == 2:
        if go[0] == 'push':
            stack.append(int(go[1]))

    else:
        if go[0] == 'top':
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
        elif go[0] == 'size':
            res.append(len(stack))

        elif go[0] == 'empty':
            if stack:
                res.append(0)
            else:
                res.append(1)

        elif go[0] == 'pop':
            if stack:
                res.append(stack.pop())
            else:
                res.append(-1)


for i in res:
    print(i)
