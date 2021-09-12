from collections import deque

def solv(priority):
    queue = deque(priority)
    temp = list(range(len(queue)))
    idx = 0

    while queue:
        if queue[0] == max(queue):
            idx += 1
            if temp[0] == M:
                res.append(idx)
                break
            else:
                temp.pop(0)
                queue.popleft()

        else:
            queue.append(queue.popleft())
            temp.append(temp.pop(0))

if __name__ == "__main__":
    res = []
    for _ in range(int(input())):
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))
        solv(priority)
    
    for i in res:
        print(i)

        

