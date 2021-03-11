from collections import deque

def solution(progresses, speeds):
    answer = list()
    subPercent = 0
    workDayList = deque()
    j = 0
    count = 1

    for i in range(len(progresses)):
        subPercent = 100 - progresses[i]
        workDay = 0
        full = 0

        while True:
            if subPercent > full:
                full += speeds[j]
                workDay += 1
            else:
                j += 1
                workDayList.append(workDay)
                break

    for i in range(1, len(workDayList)):
        if workDayList[i-count] < workDayList[i]:
            answer.append(count)
            count = 1
            
        else:
            count += 1

    answer.append(count)
    print(answer)
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])  