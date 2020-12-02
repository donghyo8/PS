def solution(s):
    answer = True

    if (len(s) == 4 or len(s) == 6) and s.isdigit() :
        answer = True
    else:
        answer = False

    print (answer)
    return answer


s = "a234"
solution(s)