S = int(input())

check = 0
for number in range(1, 4294967296):
    check += number

    if S == check:
        print(number)
        break
    elif check > S:
        print(number-1)
        break
