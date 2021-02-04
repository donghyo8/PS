def solution(n):
    answer = []
    
    # for i in str(n):
    #     answer.append(int(i))
    # print(sorted(answer, reverse=True))

    for i in reversed(str(n)):
        answer.append(int(i))
    return answer

solution(12345)