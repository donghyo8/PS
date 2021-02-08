def solution(d, budget):
    answer = 0

    d.sort()

    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break

    print(answer)
    return answer

solution([1,3,2,5,4], 9)