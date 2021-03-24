def main():
    N = int(input())
    num = str(input())
    sum = 0

    for i in range(len(num)):
        sum += int(num[i])

    print(sum)

main()