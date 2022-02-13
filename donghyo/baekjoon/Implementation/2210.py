def solv(number, x, y):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    global res

    if len(number) == 6:
        res.add(number)
        return

    else:
        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < 5 and 0 <= check_y < 5:
                solv(board[check_x][check_y] + number, check_x, check_y)


if __name__ == "__main__":
    board = [list(map(str, input().split())) for _ in range(5)]
    res = set()

    for i in range(5):
        for j in range(5):
            solv(board[i][j], i, j)

    print(len(res))
