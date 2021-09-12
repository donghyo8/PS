if __name__ == "__main__":
    arr = []
    n, m = map(int, input().split())

    for _ in range(n):
        arr.append(list(input()))

    min_value = min(n, m)
    answer = 0

    
    for i in range(n):
        for j in range(m):
            for k in range(min_value):
                if i + k < n and j + k < m:
                    if (arr[i][j] == arr[i][j + k]
                        and arr[i][j] == arr[i + k][j]
                        and arr[i][j] == arr[i + k][j + k]):
                        answer = max(answer, (k + 1) ** 2)
                print(answer)
    print(answer)


