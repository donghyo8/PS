import heapq
import sys

def solv(graph, updateList, start_city):
    queue = []
    heapq.heappush(queue, [0, start_city])
    updateList[start_city] = 0

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if updateList[current_node] < current_weight:
            continue

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if updateList[new_node] > next_weight:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [new_weight, new_node])

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
updateList = [sys.maxsize] * (N+1) 
fixed_weight = 1

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append([B, fixed_weight])

solv(graph, updateList, X)

res = []
for idx in range(1, len(updateList)):
    if updateList[idx] == K:
        res.append(idx)

if not res:
    print(-1)
else:
    for i in res:
        print(i)