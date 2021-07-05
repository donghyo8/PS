from collections import deque

def bfs(start, graph, visited, parent_Check):
    queue = deque()
    visited[start] = 1
    queue.append(start)

    while queue:
        node = queue.pop()
        print(graph[node])

        for i in graph[node]:
            if not visited[i]:
                parent_Check[i] = node
                visited[i] = 1
                queue.append(i)
    
    return parent_Check

def main():
    N = int(input())
    graph = [[] for i in range(N+1)]
    visited = [[] for i in range(N+1)]
    parent_Check = [0] * (N + 1)

    for i in range(N-1):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    result = bfs(1, graph, visited, parent_Check)

    for i in range(2, N+1):
        print(result[i])

main()