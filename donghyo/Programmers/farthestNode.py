from collections import deque

def bfs(start, n, edge):
    graph = [[] for _ in range(n)]
    visited = [0 for _ in range(n)]
    queue = deque()
    queue.append([0, 0])

    for i, j in edge:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)

    visited[0] = 1

    while queue:
        current_node, cost = queue.popleft()

        for new_node in graph[current_node]:
            if visited[new_node] == 0:
                queue.append([new_node, cost + 1])
                visited[new_node] = cost + 1

    print(visited)
    print(visited.count(max(visited)))
    return visited.count(max(visited))


def solution(n, edge):
    answer = 0
    answer = bfs(0, n, edge)

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, vertex)


