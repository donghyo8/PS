# -*- coding: utf-8 -*-
def solution(record):
    answer = []
    action = []
    dic = {}

    for i in record:
        temp = i.split(' ')
        if temp[0] == 'Enter':
            dic[temp[1]] = temp[2]
            action.append([temp[1], "님이 들어왔습니다."])

        
        elif temp[0] == 'Change':
            dic[temp[1]] = temp[2]

        else:
            del dic[temp[1]]
            action.append([temp[1], "님이 나갔습니다."])

    for uid in action:
        s = dic[uid[0]], uid[1]
        res = "".join(s)
        answer.append(res)
        
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
