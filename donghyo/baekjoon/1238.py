import heapq

def dijkstra(graph, N, X):
    answer = [0] * N
    forward_weight = list()
    queue = list()
    # updatedic = {i: float('inf') for i in range(0, len(graph))}

    for i in range(N):
        updateList = [100001] * N
        updateList[i] = 0
        heapq.heappush(queue, [updateList[i], i])

        while queue:
            current_weight, current_destination = heapq.heappop(queue)

            if updateList[current_destination] < current_weight:
                continue
            
            for new_destination, new_weight in graph[current_destination]:
                passed_weight = current_weight + new_weight

                if passed_weight < updateList[new_destination]:
                    updateList[new_destination] = passed_weight
                    heapq.heappush(queue, [passed_weight, new_destination])
        
        if i == X:
            reverse_weight = updateList
        forward_weight.append(updateList[X])

    for i in range(N):
        answer[i] = forward_weight[i] + reverse_weight[i]
        result = max(answer)
    return result

def main():
    N, M, X = map(int,input().split())
    graph = [[] for _ in range(N)]

    for i in range(M):
        startPoint, endPoint, time = map(int, input().split())
        graph[startPoint-1].append([endPoint-1, time])

    X -= 1
    print(dijkstra(graph, N, X))

main()
    
   