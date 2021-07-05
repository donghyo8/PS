from collections import deque

def solution(start, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = visited[node] + 1
                queue.append(i)

    return visited

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
visited = [0] * n
count = 0

for _ in range(1, m+1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

answer = solution(1, graph, visited)

# 노드들의 거리가 1일때는 상근이, 2면 친구, 3면은 친구에 친구, 그 이상이면 초대 X
for i in answer:
    if i > 1 and i <= 3 and i != 0:
        count += 1

print(count)