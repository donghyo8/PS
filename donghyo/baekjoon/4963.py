
def main():
    N = int(input())
    count = 0

    while N != 0:
        if N % 5 == 0:
            count += N // 5
            break
        elif N <= 0:
            count = -1
            break

        N -= 3
        count += 1
        
    print(count)
main()