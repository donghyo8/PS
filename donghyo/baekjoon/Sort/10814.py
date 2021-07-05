N = int(input())
arr = []

for i in range(N):
    arr += [list(map(str, input().split()))]

arr.sort(key=lambda x: int(x[0]))

for i in arr:
    print(i[0], i[1])
