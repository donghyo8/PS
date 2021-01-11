def solution(m, n, board):
    answer = 0

    matrix = [[board[row][col] for col in range(n)] for row in range(m)]

    for i in range(len(matrix)):
        print(matrix[i])


    return answer




m = 6 # 높이
n = 6 # 폭
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m, n, board)