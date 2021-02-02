def solution(arr, divisor):
    answer = []
    empty = -1

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if not answer:
        answer.append(empty)

    answer.sort()
    print(answer)
    return answer

solution([3,2,6], 10)