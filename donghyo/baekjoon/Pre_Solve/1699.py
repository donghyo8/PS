def solution(N):
    dp = [i for i in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, i):
            if dp[i-j*j] + 1 < dp[i]:
                dp[i] = dp[i-j*j] + 1

            if j * j > i:
                break

    print(dp[N])

N = int(input())
solution(N)