def second_max(land):
    answer = 0
    first = 0
    second = 0

    for i in range(len(land)):
        if land[i] > first:
            second = first
            first = land[i]
        elif i > second and i != first:
            second = land[i]

    answer = land.index(second)
    return answer


def solution(land):
    answer = 0
    visit1 = -1
    visit2 = -1
    validNumber = list()
    
    for i in range(len(land)):
        if visit1 != land[i].index(max(land[i])):
            validNumber.append(max(land[i]))
            visit1 = land[i].index(max(land[i]))

        else:
            visit2 = second_max(land[i])
            land[i].pop(visit1)
            validNumber.append(max(land[i]))
            visit1 = visit2
        
    for i in range(len(validNumber)):
        answer += validNumber[i]
    
    print(answer)
    return answer


land1 = [[1, 2, 3, 5],[5, 6, 7, 8],[4, 3, 2, 1]]
land2 = [[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]]
solution(land2)