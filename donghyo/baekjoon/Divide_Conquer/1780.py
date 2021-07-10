def valid(matrix):
    check = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if check != matrix[i][j]:
                return False
    return True

def cut(matrix, count):
    if valid(matrix):
        if matrix[0][0] == -1:
            count[0] += 1
        elif matrix[0][0] == 0:
            count[1] += 1
        elif matrix[0][0] == 1:
            count[2] += 1
    else:
        cut_arr = []
        length = len(matrix) // 3
        for i in range(3):
            start_idx1 = length * i
            end_idx1 = length * (i+1)

            for j in range(3):
                start_idx2 = length * j
                end_idx2 = length * (j+1)
                temp = matrix[start_idx1:end_idx1]

                for k in temp:
                    cut_arr.append(k[start_idx2:end_idx2])
                cut(cut_arr, count)
                cut_arr = []
                    
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
count = [0, 0, 0]

cut(matrix, count)
for i in count:
    print(i)
