from collections import deque
import copy

def bfs(matrix):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    global safe_Area
    queue = deque()
    copyMatrix = copy.deepcopy(matrix)

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                queue.append([i, j])
                
    while queue:
        x, y = queue.pop()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]

            if 0 <= check_x < N and 0 <= check_y < M:
                if matrix[check_x][check_y] == 0:
                    copyMatrix[check_x][check_y] = 2
                    queue.append([check_x,check_y])
    
    for i in copyMatrix:
        safe_Area += i.count(0)

    return

def setWall(wall):
    global result

    if wall == 3:
        result = max(result, bfs(matrix))
        return
    else:
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    setWall(wall + 1)
                    matrix[i][j] = 0

N, M = map(int, input().split())
matrix =[list(map(int, input().split())) for _ in range(N)]
safe_Area = 0
result = 0
setWall(0)
print(result)

