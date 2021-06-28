from collections import deque


def go(maps):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]

    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y]

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < n and 0 <= check_y < m and visited[check_x][check_y] == 0 and maps[check_x][check_y] == 1:
                visited[check_x][check_y] = visited[x][y] + 1
                queue.append([check_x, check_y])
            print(visited)

    return -1


def solution(maps):
    answer = 0
    answer = go(maps)

    # print(answer)
    return answer


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
solution(maps)
