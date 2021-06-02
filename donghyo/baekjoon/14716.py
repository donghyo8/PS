from collections import deque


def bfs(banner, visited, i, j, M, N):
    valid_x, valid_y = [1, 1, 1, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 1, -1, 0, 1]

    queue = deque()
    queue.append([i, j])

    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < M and 0 <= check_y < N and visited[check_x][check_y] == 0 and banner[check_x][check_y] == 1:
                visited[check_x][check_y] = 1
                queue.append([check_x, check_y])


M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
count = 0

for i in range(M):
    for j in range(N):
        if banner[i][j] == 1 and visited[i][j] == 0:
            bfs(banner, visited, i, j, M, N)
            count += 1

print(count)
