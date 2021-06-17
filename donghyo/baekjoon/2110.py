N, C = map(int, input().split())
location_list = [int(input()) for _ in range(N)]

location_list.sort()
s, e, res = 1, location_list[-1] - location_list[0], 0

while s <= e:
    mid = (s + e) // 2

    idx, count = 0, 1
    # for i, lo in enumerate(location_list):
    #     if lo >= location_list[idx] + mid:
    #         count += 1
    #         idx = i

    for i in range(1, len(location_list)):
        if location_list[i] >= location_list[idx] + mid:
            count += 1
            idx = i

    if count >= C:
        s = mid + 1
        res = mid
    else:
        e = mid - 1
        res = mid

print(res)
