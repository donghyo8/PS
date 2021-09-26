from collections import deque


def solv(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = [0] * (N+1)
    visited[start_node] = 1
    cnt = 0

    while queue:
        node = queue.popleft()
        cnt += 1

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    res =  []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    
    max_value = 0
    for number in range(1, N+1):
        temp = solv(graph, number)
        
        if max_value <= temp:
            if max_value < temp:
                res = []
            max_value = temp
            res.append(number)

    print(*res)
    
