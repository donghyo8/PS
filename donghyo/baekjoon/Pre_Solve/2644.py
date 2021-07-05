from collections import deque
import sys

def search(matrix, start, target, visited):
    queue = deque()
    queue.append([start, 0])

    visited[start] = 1

    while queue:
        start, count = queue.popleft()
        if start == target:
            print(count)
            sys.exit()
        for i in matrix[start]:
            if not visited[i]:
                visited[i] = 1
                queue.append([i, count + 1])
        print(queue)
    print(-1)
    

def main():
    n = int(input())
    start, target = map(int, input().split())
    m = int(input())
    matrix = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)

    search(matrix, start, target, visited)

main()