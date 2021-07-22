from itertools import combinations
N, M = map(int, input().split())

temp = []
for i in range(1, N+1):
    temp.append(i)

res = combinations(temp, M)

for i in res:
    for j in i:
        print(j, end = " ")
    print()