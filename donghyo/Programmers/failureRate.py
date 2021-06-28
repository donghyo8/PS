def solution(N, stages):
    answer = []
    temp = []
    challenge_user = len(stages)

    for stage in range(1, N+1):
        user_count = stages.count(stage)
        failureRate = 0

        if user_count == 0:
            failureRate = 0
        else:
            failureRate = user_count / challenge_user
        challenge_user -= user_count
        temp.append(failureRate)

    for _ in range(1, N+1):
        idx = temp.index(max(temp))+1
        temp[idx - 1] = -1
        answer.append(idx)

    print(answer)
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)
