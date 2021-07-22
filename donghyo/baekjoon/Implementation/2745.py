N, B = map(str, input().split())
B = int(B)

dic = {}
res = 0
alpha = 65

for i in range(10):
    dic[str(i)] = i

for i in range(10, 36):
    dic[chr(alpha)] = i
    alpha += 1

for i, j in enumerate(N[::-1]):
    print(j, i)
    res += dic[j] * (B**i)

print(res)
