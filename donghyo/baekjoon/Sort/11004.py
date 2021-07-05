N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
print(arr[K-1])
