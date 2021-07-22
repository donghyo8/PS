A, B = map(int, input().split())

temp = []
for i in range(1, 1001):
    for j in range(i):
        temp.append(i)

res = 0
for i in temp[A-1:B]:
    res += i

print(res)