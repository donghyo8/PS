def solution(x):
    answer = True
    sum = 0

    for i in str(x):
        sum += int(i)

    if x % sum == 0:
        answer = True
    else:
        answer = False

    print(answer)
    return answer

solution(13)