def solv(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 4
    else:
        return solv(number-1) + solv(number-2) + solv(number-3)


res = []
for i in range(int(input())):
    n = int(input())
    res.append(solv(n))

for i in res:
    print(i)
