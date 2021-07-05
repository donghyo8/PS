queue = []
result = []
answer = '<'

N, K = map(int, input().split())
idx = K-1

for i in range(1, N+1):
    queue.append(i)

while queue:
    if idx <= 0:
        result.append(queue[idx])
        break

    if len(queue) < K:
        idx -= 1
        queue += (queue[0:idx])
        del queue[0:idx]

    result.append(queue[idx])
    queue += (queue[0:idx])

    del queue[idx]
    del queue[0:idx]

for i in range(len(result)):
    if len(result)-1 == i:
        answer += str(result[i])
    else:
        answer += str(result[i]) + ', '
else:
    answer += '>'

print(answer)
