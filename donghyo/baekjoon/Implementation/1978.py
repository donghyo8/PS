N = int(input())
arr = list(map(int, input().split()))

res = 0
for number in arr:
    flag = False

    if number == 1:
        continue

    for idx in range(2, number):
        if number % idx == 0:
            flag = True

    if not flag:
        res += 1

print(res)
