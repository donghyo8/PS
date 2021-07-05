from collections import deque

visited = list()
global count
count = 0

def dfs(number, connetNumber, graph, startNode):
    stack = deque([startNode])
    global count
    
    if startNode in visited:
        return

    count += 1
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

def main():
    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]

    for i in range(M):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    for i in range(1, N+1):  
        dfs(M, N, graph, i)
main()
print(count)