from collections import deque

def solution(priorities, location):
    queue = deque([[p, idx] for idx, p in enumerate(priorities)])
    answer = 0

    while len(queue):
        valid = queue.popleft()

        if queue and valid[0] < max(queue)[0]:
            queue.append(valid)
        else:
            answer += 1
            if valid[1] == location:
                break
            
    print(answer)
    return answer

solution([2, 1, 3, 2], 2)