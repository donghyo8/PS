<<<<<<< HEAD
from collections import deque

def solv(start_x, start_y, snake_loc, time):
    valid_x, valid_y = [-1, 0, 1, 0], [0, 1, 0, -1]
    queue = deque()
    queue.append([start_x, start_y])
    matrix[start_x][start_y] = 1
    direction = 1

    while True:
        start_x, start_y = start_x + valid_x[direction], start_y + valid_y[direction]

        if 0 <= start_x < N and 0 <= start_y < N:

            # 이동한곳에 사과가 있으면 사과를 없애고 다음칸에 머리 위치(꼬리 움직임 X)
            if matrix[start_x][start_y] == 2:
                matrix[start_x][start_y] = 1
                queue.append([start_x, start_y])
                time += 1
                
            # 이동한 곳에 사과가 없으면 머리를 늘리고 꼬리 제거
            elif matrix[start_x][start_y] == 0:
                matrix[start_x][start_y] = 1
                queue.append([start_x, start_y])
                tail_x, tail_y = queue.popleft()
                matrix[tail_x][tail_y] = 0
                time += 1
        
=======

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

>>>>>>> 537197167509ad46305c36981bbdcd9d20bc07d7
        # 벽 또는 자기 몸에 부딪힐 경우 종료
        else:
            time += 1
            return time
<<<<<<< HEAD
            
=======

>>>>>>> 537197167509ad46305c36981bbdcd9d20bc07d7
        if len(snake_loc) != 0:
            if int(snake_loc[0][0]) == time:
                if snake_loc[0][1] == 'D':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4
<<<<<<< HEAD
                
                del snake_loc[0]

        for i in matrix:
            print(i)
        print()
        
            
=======

                del snake_loc[0]

>>>>>>> 537197167509ad46305c36981bbdcd9d20bc07d7

if __name__ == "__main__":
    N = int(input())
    K = int(input())

    matrix = [[0] * N for _ in range(N)]
    time = 0

    # 사과: 2, 뱀: 1
    for _ in range(K):
        apple_col, apple_row = map(int, input().split())
        matrix[apple_col-1][apple_row-1] = 2
<<<<<<< HEAD
    
    snake_loc = [list(map(str, input().split())) for _ in range(int(input()))]

=======

    snake_loc = [list(map(str, input().split())) for _ in range(int(input()))]

    snake_loc.sort(key=lambda x: (int(x[0])))
>>>>>>> 537197167509ad46305c36981bbdcd9d20bc07d7
    time = solv(0, 0, snake_loc, time)
    print(time)
