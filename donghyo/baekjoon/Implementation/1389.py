from collections import deque
import sys

def solv(graph, target_node):
    queue = deque()
    queue.append(target_node)
    visited = [0] * (N+1)

    while queue:
        current_node = queue.popleft()

        for i in graph[current_node]:
            if not visited[i]:
                visited[i] = visited[current_node] + 1
                queue.append(i)

    visited[target_node] = 0
    return sum(visited)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    res = {}

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    for target_node in range(1, N+1):
        res[target_node] = solv(graph, target_node)

    res = sorted(res.items(), key = lambda x:x[1])
    print(res[0][0])
    