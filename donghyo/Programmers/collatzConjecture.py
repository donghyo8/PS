def solution(num):
    answer = 0
    
    while True:
        if num == 1:
            break
        else:
            if num % 2 == 1:
                num = num * 3 + 1 
            else:
                num = num / 2
                
            if answer > 500:
                answer = -1
                break
        
        answer += 1

    print(answer)
    return answer

solution(626331)