from collections import deque


def solv(start):
    global parent_node
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                parent_node[i] = node
                print(parent_node)
                visited[i] = 1
                queue.append(i)

    return parent_node


global graph, visited
global parent_node

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]
parent_node = [0] * (N + 1)

for _ in range(N-1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

print(graph)

res = solv(1)

for i in res:
    if i:
        print(i)
