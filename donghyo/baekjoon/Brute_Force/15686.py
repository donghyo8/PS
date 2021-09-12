from itertools import combinations
import sys

if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    chicken, home, res = [], [], []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                chicken.append([i, j])
            elif matrix[i][j] == 1:
                home.append([i, j])
    
res = sys.maxsize
for i in combinations(chicken, M):
    temp = 0
    for j in home:
        min_value = sys.maxsize
        for k in i:
            distance = abs(k[0] - j[0]) + abs(k[1] - j[1])
            min_value = min(min_value, distance)
        temp += min_value
    res = min(res, temp)

print(res)