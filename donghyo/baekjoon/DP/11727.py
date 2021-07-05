N = int(input())

arr = [1, 3, 5]

if N > 3:
    for i in range(3, N):
        arr.append(arr[i-1]*2 + 1)

print(arr[N-1] % 10007)
