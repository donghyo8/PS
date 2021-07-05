from collections import deque

def bfs(x, y):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue = deque()
    queue.append([x, y])

    visited[x][y] = 1

    while queue:
        x, y  = queue.popleft()

        for i in range(4):
            check_x, check_y = x + valid_x[i], y + valid_y[i]
            if 0 <= check_x < N and 0 <= check_y < N:
                if visited[check_x][check_y] == 0:
                    if matrix[check_x][check_y] > current_height:
                        visited[check_x][check_y] = 1
                        queue.append([check_x,check_y])   

N = int(input())
matrix =[list(map(int, input().split())) for _ in range(N)]
safe_area, max_height  = 0, 0

# 최대 높이를 기준으로 삼기
for i in range(N):
    for j in range(N):
        if matrix[i][j] > max_height:
            max_height = matrix[i][j]

# 현재 높이와 인덱스 값으로 상하좌우의 높이가 현재 높이보다 크면 안전한 영역이라 보고 visited 리스트에 체크
for current_height in range(max_height):
    # 높이를 비교할 때마다 visited 리스트를 초기화
    visited = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and matrix[i][j] > current_height:
                bfs(i, j)
                count += 1

    if safe_area < count: safe_area = count
print(safe_area)








