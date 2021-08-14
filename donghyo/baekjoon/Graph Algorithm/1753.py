import heapq
import sys

def dijkstra(graph, start_node_number, updateList):
    queue = []
    updateList[start_node_number] = 0
    heapq.heappush(queue, [0, start_node_number])

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if updateList[current_node] < current_weight:
            continue

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_node]:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

# 다음 노드의 가중치가 저장된 현재 가중치 보다 작으면 가중치를 업데이트하기 위한 리스트
updateList = [sys.maxsize] * (V+1)

# u에서 v로 가는 가중치 w인 간선이며 단방향 그래프
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dijkstra(graph, K, updateList)

for idx in range(1, len(updateList)):
    if updateList[idx] == sys.maxsize:
        print('INF')
    else:
        print(updateList[idx])

