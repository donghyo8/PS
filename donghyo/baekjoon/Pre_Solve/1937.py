
import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    if visited[x][y]:
        return visited[x][y]

    visited[x][y] = 1

    for i in range(4):
        check_x, check_y = x + valid_x[i], y + valid_y[i]

        if 0 <= check_x < n and 0 <= check_y < n:
            if forest[x][y] < forest[check_x][check_y]:
                visited[x][y] = max(visited[x][y], dfs(check_x, check_y) + 1)

    return visited[x][y]


n = int(input())
forest = list()
visited = [[0] * n for _ in range(n)]
result = 0

for _ in range(n):
    forest.append(list(map(int, input().split())))


for i in range(n):
     for j in range(n):
        result = max(result , dfs(i, j))

print(result)