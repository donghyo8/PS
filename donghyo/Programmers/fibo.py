def solution(n):
    answer = 0
    fibo = list()

    for i in range(0, n):
        if i < 2:
            fibo.append(1)
        else:
            fibo.append(fibo[i-2] + fibo[i-1])

        if i == n-1:
            answer = fibo[i] % 1234567
        
    print(answer)
    return answer

solution(5)