def solution(n, lost, reserve):
    answer = 0

    lost_List = set(lost) - set(reserve)
    reserver_List = set(reserve) - set(lost)

    for i in reserver_List:
        if i-1 in lost_List:
            lost_List.remove(i-1)
        elif i+1 in lost_List:
            lost_List.remove(i+1)

    answer = n-len(lost_List)
    print(answer)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 2, 5]
solution(n, lost, reserve)
