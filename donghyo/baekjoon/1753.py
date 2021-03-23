import heapq
import sys

def dijkstra(start, graph, updateList):
    queue = list()
    
    updateList[start] = 0
    heapq.heappush(queue, [0, start])
    
    while queue:
        # print(updateList)
        current_weight, current_destination = heapq.heappop(queue)
        
        # updateList와 비교해 가중치가 크면 무시
        if updateList[current_destination] < current_weight:
            continue
        
        for new_destination, new_weight in graph[current_destination]:
            next_weight = current_weight + new_weight

            # 다음 노드의 가중치가 updateList에 저장된 현재 값보다 작으면 다음 노드까지의 가중치로 업데이트
            # 다음 노드까지의 가중치와 다음 노드 정보를 우선순위 큐에 넣음
            if next_weight < updateList[new_destination]:
                updateList[new_destination] = next_weight
                heapq.heappush(queue, [next_weight, new_destination])

def main():
    inf = sys.maxsize
    V, E = map(int, input().split())
    K = int(input())

    # u -> v로 가는 가중치 w를 저장하기 위한 graph
    # 최대값 저장을 위한 updateList
    graph = [[] for _ in range(V+1)]
    updateList = [inf] * (V+1)

    for _ in range(E):
        u, v, w = map(int,input().split())
        graph[u].append([v, w])

    dijkstra(K, graph, updateList)
    
    # update된 리스트를 루프돌며 조건에 따라 출력
    for i in range(1, V+1):
        if updateList[i] != inf:
            print(updateList[i])
        else:
            print("INF")
main()