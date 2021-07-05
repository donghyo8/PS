from collections import deque


def solution(M, priority):
    priority_queue = deque(priority)
    check = [0] * len(priority_queue)
    check[M] = 1
    idx = 0

    if len(priority_queue) == 1:
        return 1

    while priority_queue:
        if priority_queue[0] == max(priority_queue):
            idx += 1
            print(check)
            print(priority_queue)

            if check[0]:
                result.append(idx)
                break
            else:
                priority_queue.popleft()
                check.pop(0)

        else:
            priority_queue.append(priority_queue.popleft())
            check.append(check.pop(0))


T = int(input())
result = []

for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    res = solution(M, priority)
    result.append(res)

for i in result:
    if i:
        print(i)
