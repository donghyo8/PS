from collections import deque

def solution(n):
    answer = ''
    temp = deque()

    while n != 0:
        if n % 3 == 0:
            temp.appendleft('4')
            n = (n // 3) - 1
        else:
            temp.appendleft(str(n % 3))
            n = n // 3

    answer = "".join(temp)
    print(answer)
    return answer

solution(114)