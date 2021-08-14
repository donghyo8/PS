from itertools import permutations

N = int(input())

number, res = [N], 0
for i in number:
    permu = list(permutations(str(i), len(str(i))))

    max_value = "".join(max(permu))
    if int(max_value) % 30 == 0:
        res = int(max_value)

if res >= 1:
    print(res)
else:
    print(-1) 