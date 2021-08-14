def set_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80 and score < 90:
        return 'B'
    elif score >= 70 and score < 80:
        return 'C'
    elif score >= 50 and score < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''

    for i in range(len(scores)):
        temp = []
        for j in range(len(scores[i])):
            temp.append(scores[j][i])
        
        other_evaluation = temp[i]
        cnt = len(temp)

        if other_evaluation == max(temp):
            if temp.count(other_evaluation) < 2:
                temp[i] = 0
                cnt -= 1
        elif other_evaluation == min(temp):
            if temp.count(other_evaluation) < 2:
                temp[i] = 0
                cnt -= 1
        
        answer += set_grade(sum(temp) / cnt)
        print(temp, sum(temp)/cnt)
    print(answer)
    return answer

solution([[70,49,90],[68,50,38],[73,31,100]])