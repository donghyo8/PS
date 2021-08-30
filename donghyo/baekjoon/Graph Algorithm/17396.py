import heapq
import sys

def solv(graph, updateList, start_node):
    queue = []
    heapq.heappush(queue, [0, start_node])
    updateList[start_node] = 0

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if updateList[current_node] < current_weight:
            continue

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_node] and N_arr[new_node] == 0:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])

if __name__ == "__main__":
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    updateList = [sys.maxsize] * (N+1)
    N_arr[-1] = 0

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append([b, t])
        graph[b].append([a, t])

    solv(graph, updateList, 0)
    
    if updateList[N-1] < sys.maxsize:
        print(updateList[N-1])
    else:
        print(-1)