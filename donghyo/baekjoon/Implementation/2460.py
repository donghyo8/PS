
arr = [list(map(int, input().split())) for _ in range(10)]

res = []
total = 0
for current in arr:
    total += current[1] - current[0]
    res.append(total)

print(max(res))

