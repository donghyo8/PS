
def solution(phone_number):
    answer = ''

    for i in range(len(phone_number)-4):
        answer += "*"

    answer = phone_number.replace(phone_number[0:len(phone_number) - 4], answer)

    print(answer)
    return answer

solution("027778888")