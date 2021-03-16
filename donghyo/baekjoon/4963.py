
def main():
    N = int(input())
    count = 0

    while N != 0:
        if N % 5 == 0:
            count += N // 5
        elif N <= 0:
            count = -1

        N -= 3
        count += 1
main()