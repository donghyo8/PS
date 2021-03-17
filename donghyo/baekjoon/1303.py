from collections import deque

def bfs(i, j):
    validx, validy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    count = 1

    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + validx[i], y + validy[i]

            if 0 <= check_x < N and 0 <= check_y < M:
                if matrix[x][y] == matrix[check_x][check_y]:
                    if visited[check_x][check_y] == 0:
                        visited[check_x][check_y] = 1
                        queue.append([check_x,check_y])
                        count += 1

    return count

N, M = list(map(int, input().split()))
matrix =[list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
resultList = list()
w, b = 0, 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            temp = bfs(i, j)
            
            if matrix[i][j] == "W":
                w += temp ** 2
            else:
                b += temp ** 2

print(w, b)
