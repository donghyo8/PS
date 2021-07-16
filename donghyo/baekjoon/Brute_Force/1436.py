N = int(input())
number = 666
res = 0

while True:
    if "666" in str(number):
        res += 1
    
    if res == N:
        print(number)
        break

    number += 1
