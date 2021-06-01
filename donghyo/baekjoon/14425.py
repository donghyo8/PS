dic = {}
count = 0

N, M = map(int, input().split())

for _ in range(N):
    S = str(input())
    dic[S] = ''

for _ in range(M):
    valid = str(input())

    if valid in dic.keys():
        count += 1

print(dic)
print(count)