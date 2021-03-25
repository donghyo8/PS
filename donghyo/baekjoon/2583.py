from collections import deque

def search(x, y, graph, M, N):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque()
    queue.append([x, y])
    count = 1

    graph[x][y] = 1

    while queue:
        x, y = queue.pop()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]
            if 0 <= check_x < M and 0 <= check_y < N:
                if graph[check_x][check_y] == 0:
                    graph[check_x][check_y] = 1
                    queue.append([check_x, check_y])
                    count += 1

    return count
                    
    
def main():
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    areaList = list()
    areaCount = 0

    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        # 칸 색칠(2차원 리스트 직사각형을 뒤집어서 생각하면됨)
        for i in range(y1, y2):
            for j in range(x1, x2):
                graph[i][j] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                areaList.append(search(i, j, graph, M, N))
                areaCount += 1

    areaList.sort()
    print(areaCount)
    print(" ".join(map(str, areaList)))

main()