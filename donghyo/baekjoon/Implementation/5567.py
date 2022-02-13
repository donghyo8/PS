from collections import deque

# 모든 간선의 가중치가 같으니까 bfs가 제일 나을듯
def solv(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = visited[node] + 1
                queue.append(i)
    
    return visited
        

if __name__ == "__main__":
    n = int(input()); m = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = solv(graph, 1)
    res = 0

    print(graph)

    for target in ans:
        if 1 < target <= 3:
            res += 1
    print(res)
