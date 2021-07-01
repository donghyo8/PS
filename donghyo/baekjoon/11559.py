from collections import deque


def solution(field, puyo, i, j):
    valid_x, valid_y = [-1, -1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * len(field[0]) for _ in range(12)]
    queue = deque()
    queue.append([i, j])
    count = 1

    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < 12 and 0 <= check_y < len(field[0]):
                if field[check_x][check_y] == puyo and not visited[check_x][check_y]:
                    queue.append([check_x, check_y])
                    visited[check_x][check_y] = 1
                    count += 1

    #  뿌요 부시고 내리는 로직 필요함

    # if count >= 4:


field = [list(map(str, input())) for _ in range(12)]

for i in range(12):
    for j in range(len(field[0])):
        if field[i][j] != '.':
            count = solution(field, field[i][j], i, j)
            print(count)

for i in field:
    print(i)
