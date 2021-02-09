def solution(n):
    answer = ""
    convertNumber = 3
    temp = 0

    if n != 1:
        while n // convertNumber >= 1:
            remain = n % convertNumber
            n = n // convertNumber
            answer = str(remain) + answer

            if n < convertNumber :
                answer = str(n) + answer

        answer = answer[::-1]

        j = 1

        for i in answer[::-1]:
            temp += int(i) * j
            j = j * 3
    else:
        return 1
        
    answer = temp
    print(answer)
    return answer

solution(1)