import heapq
import sys

def solv(graph, updateList, start_node):
    queue = []
    heapq.heappush(queue, [0, start_node])
    updateList[start_node] = 0

    while queue:
        current_weight, current_node = heapq.heappop(queue)

        for new_node, new_weight in graph[current_node]:
            next_weight = current_weight + new_weight

            if next_weight < updateList[new_node]:
                updateList[new_node] = next_weight
                heapq.heappush(queue, [next_weight, new_node])
    
if __name__ == "__main__":
    
    res = []
    for _ in range(int(input())):
        n, d, c = map(int, input().split())

        graph = [[] for _ in range(n+1)]
        updateList = [sys.maxsize for _ in range(n+1)]

        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append([a, s])
        
        solv(graph, updateList, c)
        
        cnt = 0
        temp = 0
        for i in updateList:
            if sys.maxsize > i:
                if temp < i:
                    temp = i
                cnt += 1
        res.append([cnt, i])

    for i in res:
        print(' '.join(map(str, i)))
