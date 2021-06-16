N, M = map(int, input().split())
height_list = list(map(int, input().split()))
height_list.sort()
s, e = 0, max(height_list)

while s <= e:
    mid = (s + e) // 2

    cut = 0
    for i in height_list:
        if i > mid:
            cut += i - mid

    if cut >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)
