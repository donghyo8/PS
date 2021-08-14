def solution(n, computers):
    answer = 0
    stack = []
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            answer += 1
            visited[i] = True
            stack.append(i)

        while stack:
            i = stack.pop()

            for j in range(n):
                if computers[i][j] == 1 and visited[j] == False:
                    visited[j] = True
                    stack.append(j)
            print(visited)
    print(answer)
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)