from collections import deque


def melt(matrix, N, M):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                matrix[i][j] = 0


def solution(matrix, i, j):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]

    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    global count
    global flag
    count = 0
    flag = False

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < M:
                if visited[check_x][check_y] == 0 and matrix[check_x][check_y] == 0:
                    visited[check_x][check_y] = 1
                    queue.append([check_x, check_y])
                elif matrix[check_x][check_y] == 1:
                    matrix[check_x][check_y] = 2
                    count += 1

    if all(1 not in l for l in matrix):
        flag = True

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
time = 1
global count
global flag

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            solution(matrix, i, j)

            if flag:
                print(time)
                print(count)
                exit()
            time += 1

            melt(matrix, N, M)
