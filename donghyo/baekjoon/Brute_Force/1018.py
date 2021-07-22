N, M = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(N)]
res = []

for a in range(N-7):
    for b in range(M-7):
        W = 0
        B = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if matrix[i][j] != 'W':
                        W += 1
                    else:
                        B += 1
                else:
                    if matrix[i][j] != 'B':
                        W += 1
                    else:
                        B += 1
        res.append(W)
        res.append(B)

print(res)
print(min(res))
        

