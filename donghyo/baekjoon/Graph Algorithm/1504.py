import heapq
import sys

def solv(graph, start_node_number, end):
    updateList = [sys.maxsize] * (N+1)
    weight_init = 0
    updateList[start_node_number] = 0

    queue = []
    heapq.heappush(queue, [weight_init, start_node_number])

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        # 현재 노드의 가중치가 기존에 가중치보다 크면 무시
        if updateList[current_node] < current_weight:
            continue

        # 현재 노드에 연결된 노드와 가중치를 확인하며 거쳐가는 가중치들을 더해 기존 가중치보다 작으면 업데이트함
        for new_node, new_weight in graph[current_node]:
            next_weight = new_weight + current_weight 

            if next_weight < updateList[new_node]:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])

    return updateList[end]

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
v1, v2 = map(int, input().split())

res1 = solv(graph, 1, v1) + solv(graph, v1, v2) + solv(graph, v2, N)
res2 = solv(graph, 1, v2) + solv(graph, v2, v1) + solv(graph, v1, N)

# 가중치 업데이트가 안됬을 경우 -1
if res1 >= sys.maxsize and res2 >= sys.maxsize:
    print(-1)
else:
    print(min(res1, res2))