from collections import deque

def solution(matrix, i, j, n, m):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j])
    area_count = 1
    matrix[i][j] = 2

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i] , y + valid_y[i]

            if 0 <= check_x < n and 0 <= check_y < m:
                if matrix[check_x][check_y] == 1:
                    matrix[check_x][check_y] = 2
                    queue.append([check_x, check_y])
                    area_count += 1

    return area_count


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = 0
result = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
          count += 1
          result = max(result, solution(matrix, i, j, n, m))

print(count)
print(result)