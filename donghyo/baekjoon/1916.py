import heapq
import sys 

def dijkstra(start, arrive, graph, updateList):

    queue = list()
    updateList[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_weight, current_destination = heapq.heappop(queue)
   
        for new_destination, new_weight in graph[current_destination]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_destination]:
                updateList[new_destination] = next_weight
                heapq.heappush(queue, [next_weight, new_destination])

    return updateList

def main():
    inf = sys.maxsize
    N, M = int(input()), int(input())
    graph = [[] for _ in range(N+1)]
    updateList = [inf] * (N+1)

    for _ in range(M):
        start_city, arrive_city, cost = map(int, input().split())
        graph[start_city].append([arrive_city, cost])

    start, arrive = map(int, input().split())
    result = dijkstra(start, arrive, graph, updateList)

    print(result[arrive])
main()