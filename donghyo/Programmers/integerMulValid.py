import math

def solution(n):
    answer = 0

    x = math.sqrt(n)

    if x % 1 == 0:
        answer = (x + 1) ** 2
    else:
        answer = - 1
        
    print(int(answer))
    return int(answer)

solution(121)