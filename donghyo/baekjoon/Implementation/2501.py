N, K = map(int, input().split())

res = []
for i in range(1, N+1):
    if (N % i) == 0:
        res.append(i)

if len(res) < K:
    print(0)
else:
    print(res[K-1])