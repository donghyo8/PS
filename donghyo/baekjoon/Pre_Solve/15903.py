n, m = map(int, input().split())
arr = list(map(int, input().split()))
idx = 0

for _ in range(m):
    arr.sort()
    temp = arr[0] + arr[1]
    arr[0], arr[1] = temp, temp

    # if idx == n - 1:
    #     temp = arr[0] + arr[idx] 
    #     arr[0], arr[idx] = temp, temp
    #     break

    # temp = arr[idx] + arr[idx+1]
    # arr[idx], arr[idx+1] = temp, temp
    idx += 1

print(sum(arr))