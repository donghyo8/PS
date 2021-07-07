A, B = map(int, input().split())
m = int(input())
number = list(map(int, input().split()))[::-1]
res = []
temp = 0

for i in range(len(number)):
    temp += number[i] * (A**i)

while temp != 0:
    res.append(temp % B)
    temp //= B

for i in reversed(res):
    print(i, end=" ")
