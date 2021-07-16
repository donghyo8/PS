from itertools import permutations

arr = [int(input()) for _ in range(9)]
a = list((permutations(arr, 7)))

for i in a:
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
