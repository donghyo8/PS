from collections import deque


def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=" ")

    for i in graph[start]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, start):
    visited = [0 for _ in range(N+1)]
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]


for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
    graph[j].sort()

dfs(graph, V, visited)
print()
bfs(graph, V)
