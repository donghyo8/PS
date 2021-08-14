import heapq
import sys

def solv(graph, updateList, start_node, end_node, city_path):
    queue = []
    updateList[start_node] = 0
    heapq.heappush(queue, [0, start_node])

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        if updateList[current_node] < current_weight:
            continue

        if current_node == end_node:
            print(current_weight)
            path = [end_node]

            while end_node != start_node:
                path.append(city_path[end_node])
                end_node = city_path[end_node]
            
            print(len(path))
            print(*path[::-1])
            exit()

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_node]:
                updateList[new_node] = next_weight
                city_path[new_node] = current_node
                heapq.heappush(queue, [next_weight, new_node])

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
city_path = [[] for _ in range(N+1)]
updateList = [sys.maxsize] * (N+1)

for _ in range(M):
    start_city_number, end_city_number, weight = map(int, input().split())
    graph[start_city_number].append([end_city_number, weight])

start, end = map(int, input().split())
solv(graph, updateList, start, end, city_path)

    