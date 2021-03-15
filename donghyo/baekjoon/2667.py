

from collections import deque


def bfs(N, i, j, matrix):
    validx, validy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * N for _ in range(N)]
    count = 0

    queue = deque()
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()

        if visited[x][y] == 0:
            visited[x][y] = 1
            count += 1

        for i in range(4):
            check_x, check_y = x + validx[i], y + validy[i]

            if 0 <= check_x < N and 0 <= check_y < N and matrix[check_x][check_y] == 1:
                matrix[check_x][check_y] = 0
                queue.append([check_x,check_y])

    return count

def main():
    N = int(input())
    matrix =[list(map(int, input())) for _ in range(N)]
    component = 0
    sortList = list()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                sortList.append(bfs(N, i, j, matrix))
                component += 1

    print(component)
    sortList.sort()

    for i in sortList:
        print(i)

main()