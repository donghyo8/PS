from collections import deque
def solv(matrix, visited, i, j, check_token):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < M and 0 <= check_y < N:
                if not visited[check_x][check_y] and matrix[check_x][check_y] == check_token:
                    visited[check_x][check_y] = 1
                    queue.append([check_x, check_y])
                    cnt += 1
    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    res = [0, 0]

    for i in range(M):
        for j in range(N):
            if not visited[i][j] and matrix[i][j] == 'W':
                res[0] += solv(matrix, visited, i, j, 'W') ** 2
            elif not visited[i][j] and matrix[i][j] == 'B':
                res[1] += solv(matrix, visited, i, j, 'B') ** 2
    
    print(' '.join(map(str, res)))
