# 블록 2x2 체크
def fourBlockCheck(matrix, visited, m, n):
    for i in range(m-1):
        for j in range(n-1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1] and matrix[i][j] != ' ':
                visited[i][j] = 1
                visited[i][j+1] = 1
                visited[i+1][j] = 1
                visited[i+1][j+1] = 1

# 체크된 2x2 블록 제거
def boom(matrix, visited, m, n, count):
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                matrix[i] = matrix[i][:j] + [' '] + matrix[i][j+1:]
                count += 1
    return count


# 제거된 블록 채우기 -> 해당 함수 로직 다시 작성해야함(테스트케이스를 만족시키지 못함)
def fill(matrix, m, n):
    idx_list = []
    a = 0
    b = 0

    while a <= m:
        count = 0

        for j in range(m):
            if matrix[j][a] != ' ':
                count += 1
                if j == m-1:
                    idx_list.append(m - count)
        a += 1

        if len(idx_list) == m:
            for j in range(m):
                idx = idx_list[j]

                if idx != 0:
                    matrix[idx][j] = matrix[b][j]
                    matrix[b][j] = ' '

                    if matrix[idx][j] != ' ' and matrix[idx+1][j] == ' ':
                        matrix[idx+1][j] = matrix[idx-1][j]
        

def solution(m, n, board):
    answer = 0
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = board[i][j]

    while True:
        visited = [[0] * n for _ in range(m)]
        fourBlockCheck(matrix, visited, m, n)
        temp = boom(matrix, visited, m, n, 0)
        
        if temp == 0:
            break
        answer += temp

        fill(matrix, m, n)


        print(matrix)

    print(answer)
    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
