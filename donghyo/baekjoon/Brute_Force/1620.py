if __name__ == "__main__":
    N, M = map(int, input().split())

    pocketmon = {}
    number_check = []

    for i in range(1, N+1):
        name = str(input())
        pocketmon[name] = i
        number_check.append(name)

    call = [input() for _ in range(M)]

    res = []
    for i in call:
        if i.isdigit():
            res.append(number_check[int(i)-1])
        else:
            res.append(pocketmon[i])

    for i in res:
        print(i)
