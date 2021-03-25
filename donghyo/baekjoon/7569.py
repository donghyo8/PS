from collections import deque
import sys

# 시간날때 다시풀기 3차원이라 인덱스가 넘 햇갈림;; 코드 가독성도 넘떨어짐

def search(h, i, j, matrix, H, M, N):
    valid_x, valid_y = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0]
    valid_h = [0, 0, 0, 0, 1, -1]

    queue = deque()
    queue.append([h, i, j])


    while queue:
        h, x, y = queue.pop()

        for i in range(6):
            check_h, check_x, check_y = h + valid_h[i], x + valid_x[i], y + valid_y[i]

            if 0 <= check_h < H and 0 <= check_x < N and 0 <= check_y < M:
                if matrix[check_h][check_x][check_y] == 0:
                    matrix[check_h][check_x][check_y] = matrix[check_h][check_x][check_y] + 1
                    queue.append([check_h, check_x, check_y])


def main():
    M, N, H = map(int, input().split())
    matrix = list()
    flag = True
    day = 0

    for _ in range(H):
        matrix.append([list(map(int, input().split()))for _ in range(N)])

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if matrix[h][i][j] == 1:
                    search(h, i, j, matrix, H, M, N) 

    print(matrix)

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if matrix[h][i][j] == 0:
                    print(-1)
                    sys.exit()
                else:
                    day = max(day, matrix[h][i][j])
main()