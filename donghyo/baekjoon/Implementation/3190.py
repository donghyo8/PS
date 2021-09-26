
from collections import deque


def solv(idx_x, idx_y, snake_loc, time):
    valid_x, valid_y = [-1, 0, 1, 0], [0, 1, 0, -1]
    queue = deque()
    queue.append([idx_x, idx_y])
    matrix[idx_x][idx_y] = 1
    direction = 1

    while True:
        idx_x, idx_y = idx_x + valid_x[direction], idx_y + valid_y[direction]

        if 0 <= idx_x < N and 0 <= idx_y < N:

            # 이동한곳에 사과가 있으면 사과를 없애고 다음칸에 머리 위치(꼬리 움직임 X)
            if matrix[idx_x][idx_y] == 2:
                matrix[idx_x][idx_y] = 1
                queue.append([idx_x, idx_y])
                time += 1

            # 이동한 곳에 사과가 없으면 머리를 늘리고 꼬리 제거
            elif matrix[idx_x][idx_y] == 0:
                matrix[idx_x][idx_y] = 1
                queue.append([idx_x, idx_y])
                tail_x, tail_y = queue.popleft()
                matrix[tail_x][tail_y] = 0
                time += 1

        # 벽 또는 자기 몸에 부딪힐 경우 종료
        else:
            time += 1
            return time

        if len(snake_loc) != 0:
            if int(snake_loc[0][0]) == time:
                if snake_loc[0][1] == 'D':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4

                del snake_loc[0]


if __name__ == "__main__":
    N = int(input())
    K = int(input())

    matrix = [[0] * N for _ in range(N)]
    time = 0

    # 사과: 2, 뱀: 1
    for _ in range(K):
        apple_col, apple_row = map(int, input().split())
        matrix[apple_col-1][apple_row-1] = 2

    snake_loc = [list(map(str, input().split())) for _ in range(int(input()))]

    snake_loc.sort(key=lambda x: (int(x[0])))
    time = solv(0, 0, snake_loc, time)
    print(time)
