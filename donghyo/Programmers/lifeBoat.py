from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    
    while queue:
        temp = queue.pop()

        if queue and temp + queue[0] <= limit:
            queue.popleft()
        answer += 1

    print(answer)
    return answer

solution([70, 50, 80], 100)
     