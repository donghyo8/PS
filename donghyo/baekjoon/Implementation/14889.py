from itertools import combinations
import sys

if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    idx_list = list(range(N))
    min_value = sys.maxsize

    for i in combinations(idx_list, N // 2):
        score = [0, 0]
        start = list(i)
        link = list(set(idx_list) - set(i))
        start_comb = list(combinations(start, 2))
        link_comb = list(combinations(link, 2))

        for i, j in start_comb:
            score[0] += matrix[i][j] + matrix[j][i]
        
        for i, j in link_comb:
            score[1] += matrix[i][j] + matrix[j][i]

        if min_value > abs(score[0] - score[1]):
            min_value = abs(score[0] - score[1])

        if min_value == 0:
            print(min_value)
            exit()
    print(min_value)
            