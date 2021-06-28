def solution(board, moves):
    answer = 0
    N, M = len(board), len(board[0])
    stack = []

    for i in moves:
        for j in range(M):
            if board[j][i-1] != 0:

                if stack and stack[-1] == board[j][i-1]:
                    stack.pop()
                    answer += 2
                    board[j][i-1] = 0
                    break

                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
solution(board, moves)
