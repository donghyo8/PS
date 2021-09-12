from itertools import combinations
import sys

def solv(comb):
    global res
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = []
    cost_sum = 0
    
    for i, j in comb:
        cost_sum += cost[i][j]
        visited.append([i, j])
    
        for k in range(4):
            check_x, check_y = valid_x[k] + i, valid_y[k] + j

            if [check_x, check_y] not in visited:
                    visited.append([check_x, check_y])
                    cost_sum += cost[check_x][check_y]
            else:
                return

    res = min(res, cost_sum)

if __name__ == "__main__":
    res = sys.maxsize
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    candidates = [[i, j] for i in range(1, N-1) for j in range(1, N-1)]

for comb in combinations(candidates, 3):
    solv(comb)

print(res)