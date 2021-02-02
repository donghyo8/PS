import re

def removeStartEnd(tempList):
    start = None
    end = None

    if tempList[0] == '.':
        start = 1
    if tempList[-1] == '.':
        end = -1

    return tempList[start:end]

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[..]+',".", new_id)
    answer = removeStartEnd(new_id)
    
    if answer == '':
        answer = "a"
    
    if len(answer) >= 16:
        stringLength = len(answer) - 15
        answer = answer[0:-stringLength]

    answer = removeStartEnd(answer)

    if len(answer) <= 2:
        for i in range(3):
            answer += answer[-1]

            if len(answer) == 3:
                break

    print(answer)
    return answer

new_id1 = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "z-+.^."
new_id3 = "=.="
new_id4 = "123_.def"
new_id5 = "abcdefghijklmn.p"
solution(new_id1)