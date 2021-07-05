def main():
    I = list()
    N = int(input())
    start = 0
    count = 0

    for _ in range(N):
        I.append(list(map(int, input().split())))

    I.sort(key=lambda x: (x[1], x[0]))

    for i in I:
        if i[0] >= start:
            count += 1
            start = i[1]

    print(count)

main()