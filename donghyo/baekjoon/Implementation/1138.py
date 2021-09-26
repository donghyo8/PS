def solv(arr):
    res = [0] * N

    for i in range(N):
        cnt = 0
        for j in range(N):
            if cnt == arr[i] and not res[j]:
                res[j] = i + 1
                break
            elif not res[j]:
                cnt += 1
        
    print(*res)

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    solv(arr)