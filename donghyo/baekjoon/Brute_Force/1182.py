from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(1, N+1):
    comb = list(combinations(arr, i))

    for j in comb:
        if sum(j) == S:
            res += 1

print(res)