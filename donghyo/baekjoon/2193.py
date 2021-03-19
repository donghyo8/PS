def main():
    N = int(input())
    dp = [0] * 91

    for i in range(1, N+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-1]
        
    print(dp[N])
main()