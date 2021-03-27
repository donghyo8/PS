def main():
    N = int(input())
    alphaList = [list(map(str, input())) for _ in range(N)]
    weight = [0] * 26

    for i in alphaList:
        for index, j in enumerate(i):
            NoD = (len(i) - index) - 1
            weight[ord(j)-ord('A')] += 10 ** NoD

    weight.sort(reverse = True)

    sum = 0
    for i in range(9, -1, -1):
        sum += weight[9 - i] * i
    print(sum)

main()