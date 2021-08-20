s_1 = list(map(str, input()))
s_2 = list(map(str, input()))
s_3 = list(map(str, input()))

arr_2d = [[[0] * (len(s_3)+1) for _ in range(len(s_2) + 1)]
          for _ in range(len(s_1)+1)]

for i in range(1, len(s_1) + 1):
    for j in range(1, len(s_2) + 1):
        for k in range(1, len(s_3)+1):
            if s_1[i-1] == s_2[j-1] == s_3[k-1]:
                arr_2d[i][j][k] = arr_2d[i-1][j-1][k-1] + 1
            else:
                arr_2d[i][j][k] = max(arr_2d[i-1][j][k], arr_2d[i][j-1][k], arr_2d[i][j][k-1])

# print(arr_2d)
print(arr_2d[-1][-1][-1])
