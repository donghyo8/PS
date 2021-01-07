#-*-coding:utf-8-*-

def solution(dartResult):
    grade = []
    temp = ""
    for i in dartResult:
        if i.isdigit(): 
            temp += i
        if i == 'S':
            grade.append(int(temp) ** 1)
            temp = ""

        if i == 'D':
            grade.append(int(temp) ** 2)
            temp = ""

        if i == 'T':
            grade.append(int(temp) ** 3)
            temp = ""

        if i == '*': # 해당 점수와 바로전 점수 인덱스 값 2배 증가
            if len(grade) > 1:
                grade[-2] *= 2
            grade[-1] *= 2
            
        if i == '#':
            grade[-1] *= -1 # 마지막 인덱스 값 감소 
        
        answer = sum(grade, 0)
    print(answer)
    return answer


result = "1S2D*3T"
solution(result)

