from collections import deque

def bfs(graph, startNode, visited):
    queue = deque([startNode])
    visited = list()

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dfs(graph, startNode, visited):
    stack = deque([startNode])
    visited = list()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

n, m, v = map(int,input().split())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

print(graph)
print(dfs(graph, v, [False] * (n + 1)))
print(bfs(graph, v, [False] * (n + 1)))