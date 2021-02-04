def solution(s):
    answer = ''
    index = 0

    for i in s:
        if i != ' ':
            if index % 2 == 1:
                answer += i.lower()
            else:
                answer += i.upper()
            index += 1
        else:
            answer += i
            index = 0

    # i = 0
    # while True:
    #     if index == 0:
    #         answer += s[i].upper()
    #     elif index % 2 == 1:
    #         answer += s[i].lower()
    #     elif index % 2 != 1:
    #         answer += s[i].upper()
    #     else:
    #         index = 0

    #     i += 1
    #     index += 1

    #     if i == len(s):
    #         break

    print(answer)
    return answer

solution("try hello world")