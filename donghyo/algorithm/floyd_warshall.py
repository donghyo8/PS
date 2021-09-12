if __name__ == "__main__":
    N = int(input()); M = int(input())
    cost = [[0] * (N) for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        cost[a-1][b-1] = min(cost[a-1][b-1], c)

    for k in range(N):
        cost[k][k] = 0

        for i in range(N):
            for j in range(N):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    
    for i in cost:
        for j in range(N):
            if i[j] == 100000:
                i[j] = 0
            print(i[j], end=" ")
        print()