def solution(record):
    answer = []
    room = {}

    for strList in record:
        splitList = strList.split(' ')
        if splitList[0] == 'Enter' or splitList[0] == 'Change':
            room[splitList[1]] = splitList[2]
    print(room)

    for strList in record:
        strList = strList.split(' ')
        if strList[0] == 'Enter':
            answer.append(room[strList[1]] + "님이 들어왔습니다.")
        elif strList[0] == 'Leave':
            answer.append(room[strList[1]] + "님이 나갔습니다.")
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

