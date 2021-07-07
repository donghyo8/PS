N = int(input())

if N == 0:
    print(0)
else:
    res = []
    while N != 0:
        if N % -2:
            res.append('1')
            N = N // -2 + 1

        else:
            res.append('0')
            N = N // -2

    print("".join(reversed(res)))
