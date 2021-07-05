def convertMatrix(matrix_A, start_index):
    x, y = start_index

    # 3x3 convert
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if matrix_A[i][j] == 0:
                matrix_A[i][j] = 1
            else:
                matrix_A[i][j] = 0

def main():
    N, M = map(int, input().split())
    matrix_A = [list(map(int, input())) for _ in range(N)]
    matrix_B = [list(map(int, input())) for _ in range(N)]
    count = 0
    flag = True

    print(matrix_A)
    print(matrix_B)

    for i in range(N-2):
        for j in range(M-2):
            if matrix_A[i][j] != matrix_B[i][j]:
                count += 1
                convertMatrix(matrix_A, [i, j])

    flag =  [j for i in range(N) for j in range(M) if matrix_A[i][j] != matrix_B[i][j]]

 
    if flag:
        print(-1)
    else:
        print(count)

main()