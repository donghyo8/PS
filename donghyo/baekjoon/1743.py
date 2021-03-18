from collections import deque

def bfs(i, j):
    validx, validy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    count = 1

    visited[i][j] = 1

    while queue:
        x, y= queue.pop()

        for i in range(4):
            check_x, check_y = x + validx[i], y + validy[i]

            if 0 <= check_x < N and 0 <= check_y < M:
                if graph[check_x][check_y] == 1:
                    if visited[check_x][check_y] == 0:
                        visited[check_x][check_y] = 1
                        queue.append([check_x,check_y])  
                        count += 1
                        
    return count

N, M, K = list(map(int, input().split()))
graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
resultList = list()

for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            resultList.append(bfs(i, j))

print(max(resultList))