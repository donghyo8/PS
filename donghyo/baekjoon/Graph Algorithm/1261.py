from collections import deque

def bfs(matrix, visited, N, M):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([0, 0])

    visited[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < M and 0 <= check_y < N:
                if visited[check_x][check_y] == -1: 
                    if matrix[check_x][check_y] == 0: 
                        # 벽이 없을 때는 큐 맨앞에
                        visited[check_x][check_y] = visited[x][y]
                        queue.appendleft([check_x, check_y])
                    
                    else: # 벽 부술때 +1 누적
                        visited[check_x][check_y] = visited[x][y]+1
                        queue.append([check_x, check_y])

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]
bfs(matrix, visited, N, M)
print(visited[M-1][N-1])





