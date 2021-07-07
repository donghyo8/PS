import math
from itertools import combinations

t = int(input())
arr, res = [], []

for i in range(t):
    arr = list(map(int, input().split()))
    del arr[0]
    comb = list(combinations(arr, 2))
    sum = 0

    for j in comb:
        sum += math.gcd(j[0], j[1])
    res.append(sum)

for i in res:
    print(i)
