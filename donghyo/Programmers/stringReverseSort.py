def solution(s):
    answer = ''

    answer = "".join(sorted(s,reverse=True))
    print(answer)

    return answer

solution("Zbcdefg")