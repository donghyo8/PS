import sys
import heapq


def dijkstra(graph, update_list):
    queue = list()
    heapq.heappush(queue, [1, 0])
    update_list[1] = 0

    while queue:
        print(queue)
        current_destination, current_weight = heapq.heappop(queue)

        for new_start, new_destination, new_weight in graph:
            next_weight = current_weight + new_weight

            if new_start == current_destination and next_weight < update_list[new_destination]:
                print(current_destination, new_start)
                update_list[new_destination] = next_weight
                heapq.heappush(queue, [new_destination, next_weight])

            elif new_destination == current_destination and next_weight < update_list[new_start]:
                update_list[new_start] = next_weight
                heapq.heappush(queue, [new_start, next_weight])

    return update_list


def solution(N, road, K):
    answer = 0
    update_list = [float('inf')] * (N + 1)
    res = 0

    res = dijkstra(road, update_list)

    for i in res:
        if i <= K:
            answer += 1
    return answer


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
             [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
