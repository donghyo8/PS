# def convert_map(arr):
#     res_map = []

#     for i in arr:
#         need_count = len(arr) - len(bin(i)[2:])

#         if len(bin(i)[2:]) >= n:
#             res_map += [[bin(i)[2:]]]
#         else:
#             res_map += [['0'.rjust(need_count, '0') + bin(i)[2:]]]

#     return res_map


# def split_map(arr, res_map):
#     for idx_i, number_i in enumerate(arr):
#         for idx_j in range(n):
#             res_map[idx_i][idx_j] = number_i[0][idx_j]

#     return res_map

# def solution(n, arr1, arr2):
#     answer = []
#     map1, map2 = [], []
#     split_map1 = [[0] * n for _ in range(n)]
#     split_map2 = [[0] * n for _ in range(n)]
#     sum_map = [[0] * n for _ in range(n)]

#     map1 = convert_map(arr1)
#     map2 = convert_map(arr2)

#     new_map1 = split_map(map1, split_map1)
#     new_map2 = split_map(map2, split_map2)

#     for i in range(n):
#         for j in range(n):
#             if new_map1[i][j] == '1' or new_map2[i][j] == '1':
#                 sum_map[i][j] = '#'
#             else:
#                 sum_map[i][j] = " "

#     for i in sum_map:
#         answer.append("".join(i))

#     print(answer)
#     return answer


def solution(n, arr1, arr2):
    answer = []
    sum_map = []

    for idx in range(n):
        sum_map = format(arr1[idx] | arr2[idx], str(n) + 'b')
        sum_map = sum_map.replace('0', ' ')
        sum_map = sum_map.replace('1', '#')
        answer.append(sum_map)

    return answer

# 정답은 모두 맞는데 이상하게 테스트케이스를 만족시키지 못함
# 시간날 때 다시한번 작성
# 그냥 생각나는데로 작성해서 그렇지 간단하게 한다면 arr1과 arr2를 or 연산해서 2차원 배열을 합치고, replace로 0이면 공백 1이면 # 해서 가능할듯함


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]
solution(n, arr1, arr2)
