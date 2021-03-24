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

        # 이동할 updateList[new_destination]의 가중치가 현재 가중치(current_weight) + 새 가중치(new_weight) 보다 크면 새 가중치를 새 도착지로 저장
        # 힙에 새가중치랑, 새도착지를 저장하여 반복
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

    print(graph)
    start, arrive = map(int, input().split())
    result = dijkstra(start, arrive, graph, updateList)

    print(result[arrive])
main()