from collections import deque
def solv(matrix, start_idx, N, M):
    visited = [[0]*M for _ in range(N)]
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append(start_idx)
    visited[start_idx[0]][start_idx[1]] = 1

    while queue:
        x, y = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[N-1][M-1]

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < M and not visited[check_x][check_y] and matrix[check_x][check_y]:
                visited[check_x][check_y] = visited[x][y] + 1
                queue.append([check_x, check_y])

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(N)]
    print(solv(matrix, [0, 0], N, M))