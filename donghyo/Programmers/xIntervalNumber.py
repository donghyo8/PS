def solution(x, n):
    answer = []

    if x == 0:
        for i in range(n):
            answer.append(0)

    else:
        for i in range(x, x * n + x, x):
            answer.append(i)
        
    print(answer)
    return answer

solution(0, 3)