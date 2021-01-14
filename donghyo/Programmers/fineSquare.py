import math

def solution(w,h):
    if w > h:
        w, h = h ,w

    return w*h - (h + w - math.gcd(w,h))

solution(8, 12)