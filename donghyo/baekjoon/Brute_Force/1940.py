from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    arr = input().split()
    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            if int(arr[i]) + int(arr[j]) == M:
                cnt += 1
    print(cnt)

    # 메모리 초과
    # for i, j in list(combinations(arr, 2)):
    #     if int(i) + int(j) == M:
    #         cnt += 1
    #     # print(i, j)