from itertools import combinations

N, M = map(int, input().split())
ice_comb = list(combinations(range(1, N+1), 3))
not_Dealicious = [[0] * (N+1) for _ in range(N+1)]
res = 0

for i in range(M):
    x, y = map(int, input().split())
    not_Dealicious[x][y] = 1
    not_Dealicious[y][x] = 1

for i in ice_comb:
    if not_Dealicious[i[0]][i[1]] or not_Dealicious[i[0]][i[2]] or not_Dealicious[i[1]][i[2]]:
        continue
    res += 1

print(res)




