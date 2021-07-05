
N = int(input())

arr = [0] * (N+1)

for i in range(2, N+1):
    arr[i] = arr[i-1] + 1

    if i % 2 == 0 and arr[i] > arr[i//2]:
        arr[i] = arr[i//2] + 1
    if i % 3 == 0 and arr[i] > arr[i//3]:
        arr[i] = arr[i//3] + 1

print(arr)
print(arr[N])
