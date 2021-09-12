if __name__ == "__main__":
    N, K = map(int, input().split())
    temperature = list(map(int, input().split()))

    max_value =  temp = sum(temperature[:K])
    for idx in range(K, N):
        temp += temperature[idx] - temperature[idx-K]
        max_value = max(max_value, temp)
 
    print(max_value)
