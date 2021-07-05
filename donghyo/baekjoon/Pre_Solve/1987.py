from collections import deque

def search(x, y, C, R, matrix, visited):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 0

    queue = deque()
    queue.append([x, y])
    visited[x][y] = matrix[x][y]

    while queue:
        x, y = queue.pop()
        print(visited)
        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < R and 0 <= check_y < C:
                if visited[check_x][check_y] == 'temp':
                    if all(matrix[check_x][check_y] not in a for a in visited):
                        visited[check_x][check_y] = matrix[check_x][check_y]
                        queue.append([check_x,check_y])

    for i in range(R):
        for j in range(C):
            if visited[i][j] != 'temp':
                count += 1
    return count


def main():
    R, C = map(int, input().split())
    matrix =[list(map(str, input())) for _ in range(R)]
    visited = [['temp'] * C for _ in range(R)]
    result = 0

    result = search(0, 0, C, R, matrix, visited)

    print(result)

main()