def solv(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True

M = int(input())
N = int(input())

res = []
for i in range(M, N+1):
    if solv(i):
        res.append(i)

if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)
