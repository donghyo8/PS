# import heapq

def solution(priorities, location):
    answer = 0
    indexPriorityList = list()

    # for index, j in enumerate(priorities):
    #     indexPriorityList.append((index, j))
    indexPriorityList = [(i, j) for i, j in enumerate(priorities)]

    print(indexPriorityList)

    return answer

solution([2, 1, 3, 2], 2)