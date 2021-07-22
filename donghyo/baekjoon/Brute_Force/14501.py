N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if (i + arr[i][0]) <= N:
        dp[i] = arr[i][1]

        for j in range(i):
            if (j + arr[j][0]) <= i:
                dp[i] = max(dp[i], dp[j] + arr[i][1])

print(max(dp))
   