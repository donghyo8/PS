from collections import deque


def solv(A, B):
    queue = deque()
    queue.append([A, 1])
    res = -1

    while queue:
        x, cnt = queue.popleft()

        if x == B:
            res = cnt
            break

        if x * 2 <= B:
            queue.append([x * 2, cnt + 1])
        if int(str(x) + '1') <= B:
            queue.append([int(str(x) + '1'), cnt + 1])
        
    print(res)


if __name__ == "__main__":
    A, B = map(int, input().split())
    solv(A, B)
