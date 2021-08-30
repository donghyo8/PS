def convert(matrix_A, start_idx):
    x, y= start_idx

    for i in range(x, x+3):
        for j in range(y, y+3):
            if matrix_A[i][j] == 0:
                matrix_A[i][j] = 1
            else:
                matrix_A[i][j] = 0

N, M = map(int, input().split())
matrix_A = [list(map(int, input())) for _ in range(N)]
matrix_B = [list(map(int, input())) for _ in range(N)]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if matrix_A[i][j] != matrix_B[i][j]:
            cnt += 1
            convert(matrix_A, [i, j])

state = True
for i in range(N):
    for j in range(M):
        if matrix_A[i][j] != matrix_B[i][j]:
            state = False


if state:
    print(cnt)
else:
    print(-1)