def solution(n):
    answer = 0
    a, b = 1, 1
    
    # 피보나치랑 똑같음
    for i in range(n):
        a, b = b, a + b

    return a % 1000000007

print(solution(4))