from collections import deque

def solv_1(graph, start_node):
    visited = []
    stack = deque([start_node])
    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return len(visited) - 1

def solv_2(graph, start_node):
    visited = []
    queue = deque([start_node])
    queue.append(start_node)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return len(visited) - 1


if __name__ == "__main__":
    computer = int(input())
    connect_number = int(input())
    graph = [[] for _ in range(computer+1)]

    for _ in range(connect_number):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(solv_1(graph, 1))
    print(solv_2(graph, 1))