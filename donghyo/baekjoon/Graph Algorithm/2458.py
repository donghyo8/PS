if __name__ == "__main__":
    N, M = map(int, input().split())

    cost = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        cost[a-1][b-1] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if cost[i][k] == 1 and cost[k][j] == 1:
                    cost[i][j] = 1
    res = 0
    for i in range(N):
        total = 0
        for j in range(N):
            total += cost[i][j] + cost[j][i]
        
        if total == N - 1:
            res += 1
    
    print(res)


        
        