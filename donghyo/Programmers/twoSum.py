from itertools import combinations

def solution(numbers):
    answer = []
    comb = list()
    tempList = list()

    comb = list(combinations(numbers, 2))

    for i in comb:
        tempList.append(i[0] + i[1])

    answer = sorted(list(set(tempList)))
    # answer = sorted(answer)

    print(answer)
    return answer

numbers1 = [2,1,3,4,1]
numbers2 = [5,0,2,7]
solution(numbers2)