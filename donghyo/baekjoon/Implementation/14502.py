from collections import deque
from itertools import combinations
from copy import deepcopy

def solv(copy_matrix, visited, virus_location):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 0

    for x, y in virus_location:
        queue = deque()
        queue.append([x, y])
        visited[x][y] = 1

        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                check_x, check_y = x + valid_x[i], y + valid_y[i]

                if 0 <= check_x < N and 0 <= check_y < M:
                    if not copy_matrix[check_x][check_y]and not visited[check_x][check_y]:
                        visited[check_x][check_y] = 1
                        copy_matrix[check_x][check_y] = 2
                        queue.append([check_x, check_y])

    for i in range(N):
        for j in range(M):
            if copy_matrix[i][j] == 0:
                cnt += 1   
    return cnt 
                    
if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    zero_location, virus_location = [], []

    # N, M 범위가 8까지라 완탐 가능
    for i in range(N):
        for j in range(M):
            if not matrix[i][j]:
                zero_location.append([i, j])
            elif matrix[i][j] == 2:
                virus_location.append([i, j])

    wall_candidate = list(combinations(zero_location, 3))

    max_area = 0
    for wall_1, wall_2, wall_3 in wall_candidate:
        copy_matrix = deepcopy(matrix)
        visited = [[0] * M for _ in range(N)]

        copy_matrix[wall_1[0]][wall_1[1]] = 1
        copy_matrix[wall_2[0]][wall_2[1]] = 1
        copy_matrix[wall_3[0]][wall_3[1]] = 1

        max_area = max(max_area, solv(copy_matrix, visited, virus_location))
    
    print(max_area)