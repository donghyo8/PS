from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
comb = list(combinations(arr, 3))

res = []
for i in comb:
    if sum(i) <= M:
        res.append(sum(i))

print(max(res))
