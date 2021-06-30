from itertools import permutations
from collections import deque


def cal(pre_value, next_value, op):
    if op == '+':
        return pre_value + next_value
    elif op == '-':
        return pre_value - next_value
    elif op == '*':
        return pre_value * next_value


def solv(expression, op_list):

    queue = deque()
    num = ''

    for i in expression:
        if i.isdigit():
            num += i
        else:
            queue.append(num)
            queue.append(i)
            num = ''
    queue.append(num)

    for op in op_list:
        new_queue = deque()
        while queue:
            token = queue.popleft()

            if token == op:
                pre_value = new_queue.pop()
                next_value = queue.popleft()
                new_queue.append(cal(int(pre_value), int(next_value), op))

            else:
                new_queue.append(token)

        queue = new_queue
    return abs(queue[0])


def solution(expression):
    answer = 0
    res = []

    comb_op = list(permutations(['*', '+', '-'], 3))

    for comb in comb_op:
        res.append(solv(expression, comb))

    answer = max(res)
    return answer


solution("100-200*300-500+20")


# 100 - (200*300) - 500 + 20
