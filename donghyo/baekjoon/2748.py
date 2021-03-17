def main():
    n = int(input())
    fibo = [i for i in range(n + 1)]

    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, n + 1):
        fibo[i] = fibo[i-2] + fibo[i-1]

    print(fibo[n])
main()  
