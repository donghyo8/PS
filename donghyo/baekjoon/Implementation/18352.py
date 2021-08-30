import heapq
import sys

def solv(graph, updateList, start_node):
    queue = []
    heapq.heappush(queue, [0, start_node])
    updateList[start_node] = 0

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if updateList[new_node] > next_weight:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])

    return updateList

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    updateList = [sys.maxsize] * (N+1)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append([B, 1])

    temp = solv(graph, updateList, X)

    if K not in temp:
        print(-1)
    else:
        for idx, node in enumerate(temp):
            if node == K:
                print(idx)
            



    


