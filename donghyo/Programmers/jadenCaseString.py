def solution(s):
    answer = ''

    lower = s.lower()
    splitString = lower.split(" ")

    for i in splitString:
        i = i.capitalize()
        answer += i + " "
    answer = answer[:-1]

    # if len(s) > 1:
    #     while(True):
            
    #         if i == len(splitList):
    #             break

    #         if splitList[i][0].isdigit():
    #             resultList.append(splitList[i].lower())

    #         elif not splitList[i][0].isupper():
    #             result = splitList[i].lower().capitalize()
    #             resultList.append(result)
    #             answer = " ".join(resultList)
                   
    #         i += 1

    return answer


s1 = "3people unFollowed me"
s2 = "for the last week"
s3 = "hello    1woRld  "
solution(s2)