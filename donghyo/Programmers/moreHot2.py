# from collections import deque
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 0:
        maxUnHot_scov = heapq.heappop(scoville)
        secondHot_scov = heapq.heappop(scoville)
        heapq.heappush(scoville, maxUnHot_scov + (secondHot_scov * 2))
        answer += 1

        if scoville[0] >= K:
            print(answer)
            return answer

    return -1

    # 최소힙 (min-heap)
    # Push 시간 복잡도: O(log n) / Pop 시간 복잡도: O(log n)

    # for i in range(len(scoville)):
    #     queue.appendleft(scoville[i])

    # while True:
    #     maxUnhot_scov = queue[0]
    #     queue.popleft()
    #     secondhot_scov = queue[0]
    #     queue.popleft()

    #     queue.append(maxUnhot_scov + (secondhot_scov * 2))
    #     answer += 1

    #     if queue[0] < K and len(queue) != 1:
    #         break

    #     if queue[0] <= K:
    #         return -1

    # print(answer)
    # return answer

solution([1, 2, 3, 9, 10, 12], 7)