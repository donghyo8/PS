K, N = map(int, input().split())

length = []
for _ in range(K):
    length.append(int(input()))

length.sort()
s, e = 1, max(length)

while s <= e:
    mid = (s + e) // 2

    count = 0
    for i in length:
        count += i // mid

    if count >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)