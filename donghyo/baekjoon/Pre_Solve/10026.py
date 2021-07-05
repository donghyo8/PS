from collections import deque

def search(matrix, visited, i, j, N):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < N:
                if matrix[x][y] == matrix[check_x][check_y] and visited[check_x][check_y] == 0:
                        visited[check_x][check_y] = 1
                        queue.append([check_x,check_y])

def main():
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    countList = list()
    count1, count2 = 0, 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                count1 += 1
                search(matrix, visited, i, j, N)

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'G':
                matrix[i][j] == 'R'

            elif visited[i][j] == 0:
                count2 += 1
                search(matrix, visited, i, j, N)

    print(count1, count2)
main()