A = int(input())
B = int(input())

res = []
for i in reversed(str(B)):
    res.append(int(i)*A)
res.append(A*B)

for i in res:
    print(i)
