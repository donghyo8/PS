import math
import re

def solution(str1, str2):
    answer = 0
    strList1, strList2 = [], []
    str1, str2 = str1.upper(), str2.upper()
    maxLength = max(len(str1), len(str2))
    j = 1
    union = 0
    intersection = 0
    
    for i in range(maxLength):
        strList1.append(str1[i:j+1])   
        strList2.append(str2[i:j+1])

        if not bool(re.search("[A-Z]{1}[A-Z]{1}",str1[i:j+1])): 
            strList1.pop()

        if not bool(re.search("[A-Z]{1}[A-Z]{1}",str2[i:j+1])):
            strList2.pop()

        j += 1

    for i in set(strList1 + strList2):
       intersection += min(strList1.count(i), strList2.count(i))
       union += max(strList1.count(i), strList2.count(i))

    if union > 0:
        answer = math.trunc(intersection / union * 65536)
    else:
        answer = math.trunc(1 * 65536)

    print(strList1, strList2)
    print(answer)
    
    return answer

str1 = "FRANCE"
str2 = "french"
solution(str1, str2)

    # splitToken1 = list(map(''.join, zip(*[iter(str1)]*2)))
    # splitToken2 = list(map(''.join, zip(*[iter(str2)]*2)))
