from itertools import combinations
import sys

def distance(house, comb_list, min_dist):
    for i in comb_list:
        dist = abs(i[0] - house[0]) + abs(i[1] - house[1])
        min_dist = min(min_dist, dist)

    return min_dist

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
house, chicken_store = [], []
inf = sys.maxsize
result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append([i, j])
        elif matrix[i][j] == 2:
            chicken_store.append([i, j])

comb_list = list(combinations(chicken_store, M))

for i in comb_list:
    temp = 0
    for j in house:
        temp += distance(j, i, inf)
    result.append(temp)

print(min(result))