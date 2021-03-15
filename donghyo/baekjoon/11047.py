def main():
    N, K = list(map(int,input().split()))
    A = list()
    tempList = list()

    for _ in range(N):
        A.append(int(input()))

    A.sort(reverse=True)
    print(A)

    while K != 0:
        for i in A:
            r = 0
            r += K // i
            K -= r * i
            print(K)
            tempList.append(r)

main()