def solv(arr, K):
    res = []

    while arr:
        for i in range(K):
            temp = arr.pop(0)
            arr.append(temp)
        top = arr.pop(0)
        res.append(top)
    print("<" + ', '.join(map(str, res)) + ">")

if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = list(range(1, N+1))
    solv(arr, K-1)