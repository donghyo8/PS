def solution(a, b):
    answer = 0
    tempList = list()

    if len(a) == len(b):
        for i in range(len(a)):
            tempList.append(a[i] * b[i])
        for i in range(len(a)):
            answer += tempList[i]
        
    print(tempList)
    print(answer)
    return answer

solution([-1,0,1], [1,0,-1])

# 1*(-3) + 2*(-1) + 3*0 + 4*2 = 3
# (-1)*1 + 0*0 + 1*(-1) = -2