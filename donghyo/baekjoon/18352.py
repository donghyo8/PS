import heapq
import sys


def dijkstra(graph, start, updateList):
    queue = list()
    heapq.heappush(queue, [0, start])
    updateList[start] = 0

    while queue:
        current_weight, current_destination = heapq.heappop(queue)

        for new_destination, new_weight in graph[current_destination]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_destination]:
                updateList[new_destination] = next_weight
                heapq.heappush(queue, [next_weight, new_destination])

    return updateList


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
updateList = [[sys.maxsize] for _ in range(N+1)]
inf = sys.maxsize

for i in range(M):
    A, B = list(map(int, input().split()))
    graph[A].append([B, 1])

dijkstra(graph, X, updateList)

for i in range(1, N+1):
    if updateList[i] == K:
        flag = True
        print(i)

if not flag:
    print(-1)
