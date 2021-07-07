from collections import deque


def solv(graph, visited, start):
    visited[start] = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = 0

for i in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for start in range(1, N+1):
    if visited[start] == 0:
        solv(graph, visited, start)
        count += 1

print(count)
