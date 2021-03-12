from collections import deque

def dfs(number, connetNumber, graph, startNode):
    stack = deque([startNode])
    visited = list()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    for i in visited:
        if startNode == i:
            visited.pop(0)
    return len(visited)

def main():
    number = int(input())
    connetNumber = int(input())
    startNode = 1


    graph = [[] for i in range(number + 1)]

    for _ in range(connetNumber):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    print(dfs(number, connetNumber, graph, startNode))

main()