import heapq
import sys

def dijkstra(graph, updateList, start_node, end_node):
    queue = []
    heapq.heappush(queue, [0, start_node])
    updateList[start_node] = 1
    cost_path = []

    while queue:
        current_weight, current_node = heapq.heappop(queue)
        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight


            if updateList[new_node] > next_weight and next_weight < C:
                updateList[new_node] = next_weight
                cost_path.append([new_node, new_weight])
                heapq.heappush(queue, [next_weight, new_node])

    print(cost_path) 
    # max_value = cost_path[1][1]
    # for i in range(2, len(cost_path)):
    #     if max_value < cost_path[i][1]:
    #         max_value = cost_path[i][1]

    # print(max_value)



if __name__ == "__main__":
    N, M, A, B, C = map(int, input().split())

    graph = [[] * M for _ in range(N+1)]
    updateList = [sys.maxsize] * (N+1)

    for _ in range(M):
        a, b, cost = map(int, input().split())
        graph[a].append([b, cost])
        graph[b].append([a, cost])
    
    start_node = A; end_node = B; 
    dijkstra(graph, updateList, start_node, end_node)
    print(updateList)

    

