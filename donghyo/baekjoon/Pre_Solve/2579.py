def main():
    N = int(input())
    stairsList = list()

    for _ in range(N):
        stairsList.append(int(input()))

    if N == 1:
        print(stairsList[0])

    elif N == 2:
        print(stairsList[0] + stairsList[1])
        
    else:
        dp = [stairsList[0], stairsList[0] + stairsList[1], 
            max(stairsList[0]+ stairsList[2], stairsList[1] + stairsList[2])]

        for i in range(3,N):
            dp.append(max(dp[i-3] + stairsList[i-1] + stairsList[i], 
                        dp[i-2]+ stairsList[i]))

        print(dp[N-1])
        
main()