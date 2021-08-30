from collections import deque


def solv(matrix, target, visited, i, j, flag):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < N:
                if flag and not visited[check_x][check_y]:
                    if matrix[check_x][check_y] == target:
                        visited[check_x][check_y] = 1
                        queue.append([check_x, check_y])
                elif not flag and not visited[check_x][check_y]:
                    if matrix[check_x][check_y] == 'R' or matrix[check_x][check_y] == 'G':
                        visited[check_x][check_y] = 1
                        queue.append([check_x, check_y])
                elif flag == 2 and not visited[check_x][check_y]:
                    visited[check_x][check_y] = 1
                    queue.append([check_x, check_y])


if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(str, input())) for _ in range(N)]
    ans = []
    flag = 1

    for _ in range(2):
        visited = [[0] * N for _ in range(N)]
        res = [0, 0, 0]

        for i in range(N):
            for j in range(N):
                target = matrix[i][j]

                if flag:
                    if not visited[i][j]:
                        if matrix[i][j] == 'R':
                            solv(matrix, target, visited, i, j, flag)
                            res[0] += 1
                        elif matrix[i][j] == 'G':
                            solv(matrix, target, visited, i, j, flag)
                            res[1] += 1
                        else:
                            solv(matrix, target, visited, i, j, flag)
                            res[2] += 1
                else:
                    if not visited[i][j]:
                        if matrix[i][j] == 'R' or matrix[i][j] == 'G':
                            solv(matrix, target, visited, i, j, flag)
                            res[0] += 1
                        else:
                            flag = 2
                            solv(matrix, target, visited, i, j, flag)
                            res[1] += 1
                            flag = 0
        flag = 0

        ans.append(sum(res))
print(" ".join(map(str, ans)))
