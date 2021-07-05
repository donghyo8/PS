from collections import deque

def floyd(graph):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j:
                    continue
                
                if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                    visited[i][j] = 1
    return visited

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
answer = 0

for i in floyd(graph):
    answer = max(answer, sum(i))
print(answer)