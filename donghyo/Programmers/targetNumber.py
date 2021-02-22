from collections import deque

def bfs(numbers, target):
    result = 0

    queue.append([0, 0])

    while queue:
        sum, index = queue.popleft()

        if index == len(numbers):
            if sum == target:
                result += 1
        else:
            queue.append((sum + numbers[index], index + 1))
            queue.append((sum - numbers[index], index + 1))
            
    return result
    

def solution(numbers, target):
    answer = 0

    answer = bfs(numbers, target)

    print(answer)
    return answer

visited = list()
queue = deque()
solution([1, 1, 1, 1, 1], 3)