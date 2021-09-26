from collections import deque


def solv(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = [0] * (N+1)
    visited[start_node] = 1
    cnt = 0

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                cnt += 1

    return cnt


if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = map(int, input().split())

        graph = [[] for _ in range(N+1)]

        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        print(solv(graph, 1))