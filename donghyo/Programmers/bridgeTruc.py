from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # deque로 다리길이만큼 0을 박아두고 popleft를 했는데 시간 초과가 남;;
    # 루프를 돌리는게 더 비효율적인건지?
     
    queue = [0] * bridge_length

    while len(queue):
        queue.pop(0)
        answer += 1

        if truck_weights:
            if truck_weights[0] + sum(queue) <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)

    return answer

solution(2, 10, [7,4,5,6] )