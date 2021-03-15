def main():
    coin = [500, 100, 50, 10, 5, 1]
    N = int(input())
    count = 0
    tempList = list()
    N = 1000 - N

    while N != 0:
        for i in coin:
            r = 0
            r += N // i
            N -= r * i
            count += 1
            tempList.append(r)

    print(sum(tempList))
main()