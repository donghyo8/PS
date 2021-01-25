def solution(s):
    answer = [0, 0]
    convertCount, removedZero = 0, 0

    while True:
        # 루프를 돌며 s가 1이 되면 끝냄
        if s == "1":
            break
    
        else:
            # 루프를 돌며 s의 0을 다 날리기때문에 removedZero에 미리 누적
            removedZero += s.count("0")
            # 0을 없애고 바이너리 포맷으로 변경
            s = format(len(s.replace("0","")),"b") 
            convertCount += 1
            # c.append(bin(len(zeroRemoveList)).replace("0b",""))

    answer[0] = convertCount
    answer[1] = removedZero

    print(answer)
    return answer

s0 = "0111010"
s1 = "110010101001"
s2 = "01110"
s3 = "1111111"

solution(s2)