from collections import deque

def solution():
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue1 = queue2 = deque()
    queue1.append([fire[0][0], fire[0][1]])
    queue2.append([jihoon[0][0], jihoon[0][1]])

    while queue1:
        x, y = queue1.popleft()

        for i in range(4):
            check_x1, check_y1 = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x1 < R and 0 <= check_y1 < C:
                if matrix[check_x1][check_y1] != "#" and not visited_a[check_x1][check_y1]:
                    visited_a[check_x1][check_y1] = visited_a[x][y] + 1
                    queue1.append([check_x1, check_y1])

    while queue2:
        x, y = queue2.popleft()

        for i in range(4):
            check_x2, check_y2 = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x2 < R and 0 <= check_y2 < C:
                if matrix[check_x2][check_y2] != "#" and not visited_b[check_x2][check_y2]:
                    if not visited_a[check_x2][check_y2] or visited_a[check_x2][check_y2] > visited_b[x][y]+1:
                        visited_b[check_x2][check_y2] = visited_b[x][y] + 1
                        queue2.append([check_x2, check_y2])
            else:
                return visited_b[x][y] + 1

    return "IMPOSSIBLE"

R, C = map(int, input().split())

if R >= 1 and C <= 1000:
    matrix = [list(map(str, input())) for _ in range(R)]
    visited_a = visited_b = [[0] * C for _ in range(R)]
    jihoon = fire = []

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == "J":
                jihoon.append([i, j])
            elif matrix[i][j] == "F":
                fire.append([i, j])

    print(solution())
