from collections import deque


def solution(field, puyo, i, j):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0] * len(field[0]) for _ in range(12)]

    queue, boom_queue = deque(), deque()
    queue.append([i, j]), boom_queue.append([i, j])

    visited[i][j] = 1
    count = 1
    res = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < 12 and 0 <= check_y < len(field[0]):
                if field[check_x][check_y] == puyo and not visited[check_x][check_y]:
                    queue.append([check_x, check_y])
                    boom_queue.append([check_x, check_y])
                    visited[check_x][check_y] = 1
                    count += 1

    #  뿌요 부시기
    temp1, temp2, temp3 = [], [], []
    pre_token = ''
    init_token = '.'

    if count >= 4:
        for x, y in boom_queue:
            temp1.append(x), temp2.append(y)
            field[x][y] = '.'
        res += 1
        flag = True

    # 뿌요 내리기
        if temp1 and temp2:
            temp1, temp2 = max(temp1), list(set(temp2))

            for i in temp2:
                for j in range(temp1, -1, -1):
                    if field[j][i] != '.':
                        pre_token = field[j][i]
                        field[j][i] = init_token
                        temp3.append([j, i])

            for i in temp3:
                idx = 1
                for j in range(temp1, -1, -1):
                    field[j][i[1]] = pre_token

                    if idx == len(temp3):
                        break

                    idx += 1
    else:
        flag = False

    if not flag:
        return 0

    return res


field = [list(map(str, input())) for _ in range(12)]
res = 0

for i in range(12):
    for j in range(len(field[0])):
        if field[i][j] != '.':
            res += solution(field, field[i][j], i, j)

print(res)
