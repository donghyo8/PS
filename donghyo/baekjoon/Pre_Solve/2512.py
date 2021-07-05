N = int(input())
call = list(map(int, input().split()))
M = int(input())
print(call)

call.sort()
s, e = 0, max(call)

while s <= e:
    mid = (s + e) // 2

    sum = 0
    for i in call:
        if i >= mid:
            sum += mid
        else:
            sum += i

    if sum <= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)