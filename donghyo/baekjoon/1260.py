from collections import deque

def bfs(graph, startNode, visited):
    queue = deque([startNode])
    visited[startNode] = True
    result = list()

    while queue:
        node = queue.popleft()
        result.append(node)
        
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    print(visited)
    return result

n, m, v = map(int,input().split())

graph = [[] for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

print(bfs(graph, v, [False] * (n + 1)))
    


