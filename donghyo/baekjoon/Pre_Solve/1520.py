import sys
sys.setrecursionlimit(10**7)

def solv(x, y):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    if x == M - 1 and y == N - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
 
    visited[x][y] = 0

    for i in range(4):
        check_x, check_y = x + valid_x[i], y + valid_y[i]

        if 0 <= check_x < M and 0 <= check_y < N:
            if matrix[x][y] > matrix[check_x][check_y]:
                visited[x][y] += solv(check_x, check_y)

    return visited[x][y]
        

M, N = map(int, input().split())
matrix = list()

for _ in range(M):
    matrix.append(list(map(int, input().split())))

print(matrix)

visited = [[-1] * N for _ in range(M)]

print(solv(0, 0))