N = int(input())


def factorial(number):
    res = 0
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        res = number * factorial(number-1)
    return res


result = factorial(N)
