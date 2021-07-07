import math

T = int(input())
res = []
for i in range(T):
    A, B = map(int, input().split())
    res.append((A*B // math.gcd(A, B)))

for i in res:
    print(i)
