from collections import deque

def bfs(N, M, matrix, i, j, visited):
    validx, validy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    queue = deque()
    queue.append([i,j])

    visited[i][j] = 1

    while queue:
      x, y  = queue.popleft()

      if x == N - 1 and y == M - 1:
         return visited[x][y]  
          
      print(visited)

      for i in range(4):
            check_x, check_y = x + validx[i], y + validy[i]
            if 0 <= check_x < N and 0 <= check_y < M:
                if matrix[check_x][check_y] == 1:
                    if visited[check_x][check_y] == 0:
                        visited[check_x][check_y] = visited[x][y] + 1
                        queue.append([check_x,check_y])          

    
def main():
    N, M = list(map(int, input().split()))
    matrix =[list(map(int, input())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 0
    answer = bfs(N, M, matrix, 0, 0, visited)
    print(answer)

main()
