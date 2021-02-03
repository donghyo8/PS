def solution(s, n):
    answer = ''

    for i in s:
        nextAlpha = ord(i) + n

        if i != ' ':
            # z(122) -> a(97) , Z(90) -> 65(A) 
            if 65 <= ord(i) <= 90:
                if nextAlpha > 90:
                    nextAlpha = nextAlpha - 26
                temp = chr(nextAlpha)

            else:
                if nextAlpha > 122:
                    nextAlpha = nextAlpha - 26
                temp = chr(nextAlpha)

            answer += temp
        else:
            answer += ' '
    
    print(answer)
    return answer

solution("a B z", 4)