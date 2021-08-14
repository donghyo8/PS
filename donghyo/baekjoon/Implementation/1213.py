from collections import deque

s = str(input())

temp, res = [], []
queue = deque(s)

for _ in range(len(s)):
    queue.append(queue.popleft())
    temp.append(list(queue))

for candidate in temp:
    if "".join(candidate) == "".join(candidate)[::-1]:
        res.append("".join(candidate))

res = sorted(res, key=lambda x:x[0])

if res:
    print(res[0])
else:
    print("I'm Sorry Hansoo")