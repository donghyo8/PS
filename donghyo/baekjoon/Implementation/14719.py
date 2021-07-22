H, W = map(int, input().split())
matrix = [[0] * W for _ in range(H)]
block_height = list(map(int, input().split()))

for i in range(len(matrix[0])):
    current = block_height[i]
    block_cnt = 0
    
    for j in range(len(matrix)-1, -1, -1):
        if current == block_cnt:
            break
        else:
            matrix[j][i] = 1
        block_cnt += 1

temp = []
for i in range(len(matrix)):
    one_count, cursor = 0, 0

    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            one_count += 1
            if cursor != 0 and one_count >= 2:
                temp.append(cursor)
            cursor = 0
        else:
            cursor += 1

print(sum(temp))
