import heapq
import sys

def dijkstra(start, arrive_candidateList, g, h, graph, n):
    queue = list()
    passed_List = list()
    result_List = list()

    updateList = [sys.maxsize] * (n + 1)
    updateList[start] = 0

    heapq.heappush(queue, [0, start])
    passed_List.append(start)
    
    while queue:
        current_weight, current_destination = heapq.heappop(queue)

    
        for new_destination, new_weight in graph[current_destination]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_destination]:
                updateList[new_destination] = next_weight
                heapq.heappush(queue, [next_weight, new_destination])
                
                # ! 출발지(g)부터 도착지(h)를 지나는지 검사하고 목적지들 중 불가능한 목적지를 제외하는 코드 추가해야함

                passed_List.append(new_destination)

    for i in range(len(passed_List)):
        if passed_List[i] in arrive_candidateList:
            result_List.append(passed_List[i])
            
    result_List.sort()
    return result_List

def main():
    T = int(input())
    resultList = list()

    for _ in range(T): # T
        # 교차로, 도로, 목적지 후보의 개수
        n, m, t = map(int, input().split())
        graph = [[] for _ in range(n + 1)]

        # 예술가들의 출발지, 지나간 노드 시작, 지나간 노드 도착
        s, g, h = map(int, input().split())

        for _ in range(m):
            # a, b 사이에 길이 d의 양방향 도로가 있음을 의미
            a, b, d = map(int, input().split())
            graph[a].append([b, d])

        # 목적지 후보
        x = list()
        for _ in range(t): # t
            x.append(int(input()))

        resultList.append(dijkstra(s, x, g, h, graph, n))

    print(resultList)

    for i in resultList:
        print(" ".join(str(i)))


main()