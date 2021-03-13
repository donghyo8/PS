from collections import deque


def bfs(M, N, i, j, graph):
    validx, validy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append([j, i])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            check_x, check_y = x + validx[i], y + validy[i]

            if 0 <= check_x < N and 0 <= check_y < M and graph[check_x][check_y] == 1:
                graph[check_x][check_y] = 0
                queue.append([check_x,check_y])

def main():
    T = int(input())
    
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0] * M for _ in range(N)]
        result = 0

        for _ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1


        for i in range(M):
            for j in range(N):
                if graph[j][i] == 1:
                    bfs(M, N, i, j, graph)
                    result += 1
        print(result)
main()