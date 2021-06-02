from collections import deque

def bfs(matrix, visited, M):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
       x, y = queue.popleft()

       if x == M:
           return print("YES")
           
       for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < N:
               if matrix[check_x][check_y] == 0 and visited[check_x][check_y] == 0:
                    print(check_x, check_y)
                    visited[check_x][check_y] = 1
                    queue.append([check_x, check_y])
    
    print("NO")
        
M, N = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
queue = deque()

for j in range(N):
    if matrix[0][j] == 0:
        visited[0][j] = 1
        queue.append([0, j])

bfs(matrix, visited, M-1)
