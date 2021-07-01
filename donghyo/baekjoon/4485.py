import heapq


def solution(matrix, N, count):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    update_list = [[float('inf')]*N for _ in range(N)]
    queue = list()
    heapq.heappush(queue, [0, 0, matrix[0][0]])
    update_list[0][0] = 0

    while queue:
        x, y, weight = heapq.heappop(queue)

        if x == N-1 and y == N-1:
            print("Problem {0}: {1}".format(count, weight))
            break

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < N:
                new_weight = weight + matrix[check_x][check_y]

                # 최소 가중치 갱신
                if new_weight < update_list[check_x][check_y]:
                    update_list[check_x][check_y] = new_weight
                    heapq.heappush(queue, [check_x, check_y, new_weight])


count = 1
while True:
    N = int(input())

    if N == 0:
        exit()

    matrix = [list(map(int, input().split())) for _ in range(N)]
    solution(matrix, N, count)
    count += 1
