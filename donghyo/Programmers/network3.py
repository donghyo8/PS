# DFS
def solution(n, computers):
    answer = 0
    visited = list([0 for i in range(n)])
    stack = list()
    current = 0

    for i in range(n):
        if visited[i] != 1:
            answer += 1
            visited[i] = True
            stack.append(i)

        while stack:
            current = stack[-1]
            stack.pop()

            for j in range(n):
                if computers[current][j] == True and visited[j] == False:
                    visited[j] = True
                    stack.append(j)

    print(answer)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)