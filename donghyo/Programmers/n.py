import math

def lcm(x, y):
    res = x * y // math.gcd(x, y)
    print(res)
    return res

def solution(arr):
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        print(arr)
        if len(arr) == 1:
            return arr[0]

print(solution([2, 6, 8, 14]))
