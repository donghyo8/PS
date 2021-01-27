from itertools import combinations

def validDecimal(num):
    if(num < 2):
        return False

    for i in range(2, num):
        if(num % i == 0):
            return False

    return True

def solution(nums):
    answer = 0
    tempList = list()
    resultList = list()
    boolList = list()
    sum = 0
    flag = 0

    removedDup = list(set(nums))
    temp = list(combinations(removedDup, 3))

    for i in range(len(temp)):
        for j in range(3):
            tempList.append(temp[i][j])


    for i in range(len(tempList)):
        sum += tempList[i]
        flag += 1

        if flag == 3:
            resultList.append(sum)
            sum = 0
            flag = 0

    for i in range(len(resultList)):
        boolList.append(validDecimal(resultList[i]))
        if boolList[i] == True:
            answer += 1

    print(resultList)
    print(boolList)
    print(answer)
    
    return answer

nums1 = [1,2,3,4]
nums2 = [1,2,7,6,4]
solution(nums2)