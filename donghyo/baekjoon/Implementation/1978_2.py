def solv(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True

N = int(input())
arr = list(map(int, input().split()))

res = 0
for n in arr:
    if solv(n):
        res += 1

print(res)
