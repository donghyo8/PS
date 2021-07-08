from collections import deque


def bfs(matrix, visited, i, j):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    side_island_loc = []
    queue.append([i, j])

    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < N:
                if matrix[check_x][check_y] == 0 and [x, y] not in side_island_loc:
                    side_island_loc.append([x, y])

                if visited[check_x][check_y] == 0 and matrix[check_x][check_y] == 1:
                    visited[check_x][check_y] = 1
                    queue.append([check_x, check_y])

    return side_island_loc


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
island_count = 0
side_island_loc = []
res = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == 0:
            side_island_loc.append(bfs(matrix, visited, i, j))
            island_count += 1

# 바다를 접하는 좌표 리스트로 다른 섬과의 최소거리 계산하는 로직 추가해야함
for i in side_island_loc:
    print(i)
