from collections import deque

# BFS
def solution(n, computers):
    answer = 0
    visited = list([0 for i in range(n)])
    queue = deque(maxlen=200)
    current = 0

    for i in range(n):
        if visited[i] != 1:
            answer += 1
            visited[i] = True
            queue.append(i)

        while queue:
            current = queue[0]
            queue.popleft()

            for j in range(n):
                if computers[current][j] == True and visited[j] == False:
                    visited[j] = True
                    queue.append(j)

    print(visited)
    print(answer)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)