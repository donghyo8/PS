def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    limit = int(sum ** 0.5)
    temp = 0

    for i in range(3, limit+1):
        if sum % i == 0:

            temp = sum // i

            if ((temp - 2) * (i - 2) == yellow):
                answer.append(temp)
                answer.append(i)
                break

    return answer

solution(10, 2)