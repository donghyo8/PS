from itertools import permutations

arr = [(int(input())) for _ in range(9)]
per = list(permutations(arr, 7))

res = []
for i in per:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break