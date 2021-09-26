import heapq
import sys


def dijkstra(graph, s, t):
    queue = []
    updateList = [sys.maxsize] * (n+1)
    updateList[s] = 0
    heapq.heappush(queue, [0, s])

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if updateList[current_node] < current_weight:
            continue

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_node]:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])

    return updateList[t]


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    updateList = [sys.maxsize] * (n+1)

    for _ in range(m):
        a, b, weight = map(int, input().split())
        graph[a].append([b, weight])
        graph[b].append([a, weight])
    s, t = map(int, input().split())

    print(dijkstra(graph, s, t))
