N = int(input())
arr = [0] * N


def recursive(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if arr[N-1]:
        return arr[N-1]
    else:
        arr[N-1] = recursive(N-1) + recursive(N-2)
        return arr[N-1]


print(recursive(N) % 10007)
