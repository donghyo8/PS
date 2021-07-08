import sys
sys.setrecursionlimit(1000001)


def solv(matrix, visited, x, y, n):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[x][y] = 1
    global count

    if matrix[x][y] == 1:
        count += 1

    for i in range(4):
        check_x, check_y = x + valid_x[i], y + valid_y[i]

        if 0 <= check_x < n and 0 <= check_y < n:
            if not visited[check_x][check_y] and matrix[check_x][check_y]:
                solv(matrix, visited, check_x, check_y, N)

    return count


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

global count
area_count = 0
res = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] and not visited[i][j]:
            count = 0
            res.append(solv(matrix, visited, i, j, N))
            area_count += 1

print(area_count)
for i in sorted(res):
    print(i)
