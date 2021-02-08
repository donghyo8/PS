from math import gcd

def solution(n, m):
    answer = []

    answer.append(gcd(n, m))
    answer.append(n * m // gcd(n, m))
    
    print(answer)
    return answer

solution(2, 5)