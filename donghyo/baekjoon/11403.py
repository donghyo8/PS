def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    for i in graph:
        for j in i:
            print(j, end = " ")
        print()

solution()