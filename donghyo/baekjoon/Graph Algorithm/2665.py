from collections import deque

def dijkstra():
    pass

def bfs(matrix, visited, N):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = valid_x[i] + x, valid_y[i] + y

            if 0 <= check_x < N and 0 <= check_y < N:
                if visited[check_x][check_y] == -1:
                    if matrix[check_x][check_y] == 0:
                        visited[check_x][check_y] = visited[x][y] + 1
                        queue.append([check_x, check_y])
                    else:
                        visited[check_x][check_y] = visited[x][y]
                        queue.appendleft([check_x, check_y])

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

bfs(matrix, visited, N)
print(visited[N-1][N-1])



