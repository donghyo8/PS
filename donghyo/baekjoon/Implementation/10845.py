from collections import deque
import sys

queue = deque()
res = []
N = int(input())

for i in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        if command[0] == 'push':
            queue.append(int(command[1]))

    else:
        if command[0] == 'pop':
            if queue:
                res.append(queue.popleft())
            else:
                res.append(-1)

        elif command[0] == 'size':
            res.append(len(queue))

        elif command[0] == 'empty':
            if queue:
                res.append(0)
            else:
                res.append(1)

        elif command[0] == 'front':
            if queue:
                res.append(queue[0])
            else:
                res.append(-1)
        elif command[0] == 'back':
            if queue:
                res.append(queue[-1])
            else:
                res.append(-1)

for i in res:
    print(i)
