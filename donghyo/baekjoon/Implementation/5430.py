from collections import deque

def reverse(arr):
    queue = deque()
    for idx in range(len(arr)-1, -1, -1):
        queue.append(arr[idx])
    return list(queue)


def delete(arr):
    queue = deque()

    if len(arr) == 0 or n == 0:
        return "error"
    else:
        for number in arr:
            queue.append(number)

    queue.popleft()
    return list(queue)

if __name__ == "__main__":
    res = []
    for _ in range(int(input())):
        p_function = str(input())
        n = int(input())
        arr = input()[1:-1].split(',')

        for idx, command in enumerate(p_function):
            if command == 'R':
                arr = reverse(arr)
            elif command == 'D':
                arr = delete(arr)

        if arr == "error":
            res.append(arr)
        else:
            res.append("[" + ",".join(arr) + "]")

for i in res:
    print(i)
