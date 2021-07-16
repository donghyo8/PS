N, M = map(int, input().split())
DNA = [str(input()) for _ in range(N)]
res = ""
count = 0

for i in range(M):
    a = [0 for _ in range(26)]

    for j in range(N):
        a[ord(DNA[j][i]) - 65] += 1
    res += chr(a.index(max(a)) + 65)

for i in range(N):
    for j in range(M):
        if DNA[i][j] != res[j]:
            count += 1

print(res)
print(count)
