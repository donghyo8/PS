def solution(price, money, count):
    answer = -1
    mul = 0
    for i in range(1, count + 1):
        mul += price * i

    answer = abs(mul) - abs(money)

    if answer > 0:
        return answer
    else:
        answer = 0
    return answer

solution(3, 20, 4)