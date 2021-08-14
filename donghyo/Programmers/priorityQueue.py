from collections import deque

def solution(operations):
    queue = deque()
    
    for i in operations:
        temp = i.split()

        if temp[0] == 'I':
            queue.append(temp[1])

        elif temp[0] == 'D':
            if not queue:
                continue
            elif int(temp[1]) > 0:
                queue.remove(max(queue))

            elif int(temp[1]) < 0:
                numbers = []
                for i in queue:
                    if int(i) < 0:
                        numbers.append(i)
                max_value = max(numbers)
                queue.remove(max_value)
                
    if not queue:
        print([0, 0])
        return [0, 0]
    else:
        res = list(map(int, queue))
        return res

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])