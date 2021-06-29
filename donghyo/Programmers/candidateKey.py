# from functools import cmp_to_key

# def check(relation, row_length, col_length, subset):
#     for i in range(row_length - 1):
#         for j in range(i+1, row_length):
#             flag = True

#             for k in range(col_length):
#                 if (subset & 1 << k) == 0:
#                     continue
#                 if relation[i][k] != relation[j][k]:
#                     flag = False
#                     break
#             if flag:
#                 return False

#     return True


# def compare(a, b):
#     x = bin(a).count('1')
#     y = bin(b).count('1')

#     return x - y

# # def uniqueness(relation):
# #     count, idx = 0, 0
# #     for i in range(len(relation[0])):
# #         valid_distinct = []
# #         for j in range(len(relation)):
# #             valid_distinct.append(relation[j][i])

# #         if len(valid_distinct) == len(set(valid_distinct)):
# #             idx = i
# #             count += 1
# #         print(valid_distinct, set(valid_distinct))

# #     return count, idx


# def solution(relation):
#     answer = 0
#     row_length, col_length = len(relation), len(relation[0])
#     candidates = []

#     for i in range(1, 1 << col_length):
#         if check(relation, row_length, col_length, i):
#             candidates.append(i)

#     candidates = sorted(candidates, key=cmp_to_key(compare))
#     print(candidates)

#     while len(candidates) != 0:
#         n = candidates.pop(0)
#         answer += 1
#         candidates = [i for i in candidates if (n & i) != n]

#     print(answer)
#     return answer


# relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
#     "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
# solution(relation)
