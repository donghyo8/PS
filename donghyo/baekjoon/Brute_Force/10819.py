from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

sequence_number = list(permutations(A, N))
res = []

for i in sequence_number:
    sum = 0
    for j in range(N-1):
        sum += abs(i[j] - i[j+1])
    res.append(sum)

print(max(res))
