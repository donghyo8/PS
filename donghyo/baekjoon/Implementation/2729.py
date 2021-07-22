res = []
for _ in range(int(input())):
    A, B = map(int, input().split())
    A = int('0b' + str(A), 2)
    B = int('0b' + str(B), 2)
    sum = A + B
    res.append(bin(sum)[2:])

for i in res:
    print(i)
