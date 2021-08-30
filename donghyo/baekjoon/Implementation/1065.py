N = int(input())

res = 0
for i in range(1, N+1):
    number = list(map(int, str(i)))
    print(number)
    
    if i <= 99:
        res += 1
    elif number[0] - number[1] == number[1] - number[2]:
        res += 1

print(res)