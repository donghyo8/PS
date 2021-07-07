from collections import deque
N, K = map(int, input().split())

arr = deque()
res = []
for i in range(N):
    arr.append(i+1)

while arr:
    arr.rotate(-(K-1))  # - 앞, + 뒤 기준으로
    res.append(arr[0])
    del arr[0]

print("<", end='')
for i in res[:-1]:
    print(i, end=', ')
print(res[-1], end='')
print('>')
