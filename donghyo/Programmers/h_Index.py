def solution(citations):
    answer = 0
    
    citations.sort(reverse = True)

    for i in range(len(citations)):
        if citations[i] <= i and citations[i] != 0:
            answer = i
            break

        if citations[i] >= len(citations):
            answer = len(citations)

    print(answer)
    return answer


citations = [5, 5, 5, 5, 5]
solution(citations)