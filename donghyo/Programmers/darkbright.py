def solution(absolutes, signs):
    answer = 123456789
    plus = []
    minus = []
    idx = 0

    for valid in signs:
        if valid == True:
            plus.append(absolutes[idx])
        else:
            minus.append(absolutes[idx])

        idx += 1
        
    answer = sum(plus) - sum(minus)
    print(answer)
    return answer

solution([1, 2, 3], [False, False, True])
