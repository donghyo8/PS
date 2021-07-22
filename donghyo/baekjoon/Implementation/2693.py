res = []
for i in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    res.append(arr[-3])

for i in res:
    print(i)