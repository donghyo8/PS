    N = int(input())
    array = list(map(int, input().split()))
    resultList = [0] * 100

    resultList[0] = array[0]
    resultList[1] = max(array[0], array[1]) 

    for i in range(2, N):
        resultList[i] = max(resultList[i-1], resultList[i-2] + array[i])

    print(resultList[N-1])