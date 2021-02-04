def solution(n):
    answer = 0
    tempList = list()

    for i in str(n):
        tempList.append(i)

    return int("".join(sorted(tempList, reverse=True)))

solution(118372)