def main():
    length = list()
    N = int(input())
    length = list(map(int,input().split()))
    price = list(map(int,input().split()))

    result = 0
    temp = price[0]

    for i in range(N-1):
        if price[i] <= temp:
            temp = price[i]
        
        result += temp * length[i]
    print(result)

main()