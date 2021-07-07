A, P = map(int, input().split())
res = [A]

while True:
    temp = 0
    for i in str(res[-1]):
        temp += int(i) ** P
    print(temp)

    if temp in res:
        break

    res.append(temp)

print(res.index(temp))
